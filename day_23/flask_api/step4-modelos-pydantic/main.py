from typing import List, Optional

from flask import Flask, jsonify, request
from pydantic import BaseModel, Field, ValidationError

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)
    priority: int = Field(default=3, ge=1, le=5)
    done: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=80)
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    done: Optional[bool] = None


class TaskOut(BaseModel):
    id: int
    title: str
    priority: int
    done: bool


tasks: List[TaskOut] = [
    TaskOut(id=1, title="Preparar ejercicios", priority=2, done=False),
    TaskOut(id=2, title="Corregir tareas", priority=4, done=True),
]


def model_to_dict(model: BaseModel) -> dict:
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_none=True)
    return model.dict(exclude_none=True)


def to_json(model: BaseModel) -> dict:
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


def get_task_or_none(task_id: int) -> Optional[TaskOut]:
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def parse_payload(model_cls):
    payload = request.get_json(silent=True)
    if payload is None:
        return None, jsonify({"detail": "Body JSON requerido"}), 400

    try:
        return model_cls(**payload), None, None
    except ValidationError as exc:
        return None, jsonify({"detail": exc.errors()}), 422


@app.get("/tasks")
def list_tasks():
    return jsonify([to_json(task) for task in tasks])


@app.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    task = get_task_or_none(task_id)
    if task is None:
        return jsonify({"detail": "Tarea no encontrada"}), 404
    return jsonify(to_json(task))


@app.post("/tasks")
def create_task():
    payload, error_response, status_code = parse_payload(TaskCreate)
    if error_response is not None:
        return error_response, status_code

    data = model_to_dict(payload)
    new_task = TaskOut(id=max((task.id for task in tasks), default=0) + 1, **data)
    tasks.append(new_task)
    return jsonify(to_json(new_task)), 201


@app.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    task = get_task_or_none(task_id)
    if task is None:
        return jsonify({"detail": "Tarea no encontrada"}), 404

    payload, error_response, status_code = parse_payload(TaskUpdate)
    if error_response is not None:
        return error_response, status_code

    data = model_to_dict(payload)
    updated_task = task.model_copy(update=data) if hasattr(task, "model_copy") else task.copy(update=data)

    index = tasks.index(task)
    tasks[index] = updated_task
    return jsonify(to_json(updated_task))


if __name__ == "__main__":
    app.run(debug=True)
