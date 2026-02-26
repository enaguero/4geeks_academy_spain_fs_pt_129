from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Step 3 - CRUD en memoria")

tasks: List[Dict[str, Any]] = [
    {"id": 1, "title": "Preparar clase de API", "done": False},
    {"id": 2, "title": "Crear primer endpoint", "done": True},
]


def find_task(task_id: int) -> Optional[Dict[str, Any]]:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


@app.get("/tasks")
def list_tasks(done: Optional[bool] = None):
    if done is None:
        return tasks
    return [task for task in tasks if task["done"] == done]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: Dict[str, Any]):
    title = str(payload.get("title", "")).strip()
    if not title:
        raise HTTPException(status_code=400, detail="El campo 'title' es requerido")

    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "done": bool(payload.get("done", False)),
    }
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: Dict[str, Any]):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    if "title" in payload:
        title = str(payload["title"]).strip()
        if not title:
            raise HTTPException(status_code=400, detail="El title no puede estar vacio")
        task["title"] = title

    if "done" in payload:
        task["done"] = bool(payload["done"])

    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tasks.remove(task)
    return {"message": "Tarea eliminada", "task_id": task_id}
