from typing import Any, Dict, List, Optional

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


tasks: List[Dict[str, Any]] = [
    {"id": 1, "title": "Preparar clase de API", "done": False},
    {"id": 2, "title": "Crear primer endpoint", "done": True},
]


def find_task(task_id: int) -> Optional[Dict[str, Any]]:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def parse_bool_query(value: str) -> Optional[bool]:
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    return None


@app.errorhandler(404)
def handle_not_found(error):
    message = getattr(error, "description", "Recurso no encontrado")
    return jsonify({"detail": message}), 404


@app.get("/tasks")
def list_tasks():
    done_arg = request.args.get("done")
    if done_arg is None:
        return jsonify(tasks)

    done = parse_bool_query(done_arg)
    if done is None:
        return jsonify({"detail": "done debe ser true o false"}), 400

    filtered = [task for task in tasks if task["done"] == done]
    return jsonify(filtered)


@app.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        return jsonify({"detail": "Tarea no encontrada"}), 404
    return jsonify(task)


@app.post("/tasks")
def create_task():
    payload = request.get_json(silent=True) or {}
    title = str(payload.get("title", "")).strip()

    if not title:
        return jsonify({"detail": "El campo 'title' es requerido"}), 400

    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "done": bool(payload.get("done", False)),
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        return jsonify({"detail": "Tarea no encontrada"}), 404

    payload = request.get_json(silent=True) or {}

    if "title" in payload:
        title = str(payload["title"]).strip()
        if not title:
            return jsonify({"detail": "El title no puede estar vacio"}), 400
        task["title"] = title

    if "done" in payload:
        task["done"] = bool(payload["done"])

    return jsonify(task)


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        return jsonify({"detail": "Tarea no encontrada"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarea eliminada", "task_id": task_id})


if __name__ == "__main__":
    app.run(debug=True)
