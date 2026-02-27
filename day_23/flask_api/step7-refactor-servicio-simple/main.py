from typing import Optional

from flask import Flask, jsonify, request
from pydantic import ValidationError

import service
from schemas import TaskCreate, TaskUpdate

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


def model_to_dict(model):
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


def parse_bool_query(name: str) -> Optional[bool]:
    raw = request.args.get(name)
    if raw is None:
        return None

    value = raw.strip().lower()
    if value in {"true", "1", "yes"}:
        return True
    if value in {"false", "0", "no"}:
        return False

    raise service.AppError(status_code=400, detail=f"{name} debe ser true o false")


def parse_payload(model_cls):
    payload = request.get_json(silent=True)
    if payload is None:
        raise service.AppError(status_code=400, detail="Body JSON requerido")

    try:
        return model_cls(**payload)
    except ValidationError as exc:
        raise service.AppError(status_code=422, detail=exc.errors())


@app.errorhandler(service.AppError)
def handle_app_error(error: service.AppError):
    return jsonify({"detail": error.detail}), error.status_code


@app.get("/tasks")
def list_tasks():
    done = parse_bool_query("done")
    tasks = service.list_tasks(done)
    return jsonify([model_to_dict(task) for task in tasks])


@app.post("/tasks")
def create_task():
    payload = parse_payload(TaskCreate)
    task = service.create_task(payload)
    return jsonify(model_to_dict(task)), 201


@app.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    payload = parse_payload(TaskUpdate)
    task = service.update_task(task_id, payload)
    return jsonify(model_to_dict(task))


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    service.delete_task(task_id)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
