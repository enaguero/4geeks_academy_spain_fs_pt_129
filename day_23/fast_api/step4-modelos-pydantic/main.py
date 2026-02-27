from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Step 4 - Pydantic y validacion")


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


def get_task_or_404(task_id: int) -> TaskOut:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@app.get("/tasks", response_model=List[TaskOut])
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    return get_task_or_404(task_id)


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    data = model_to_dict(payload)
    new_task = TaskOut(id=max((task.id for task in tasks), default=0) + 1, **data)
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate):
    task = get_task_or_404(task_id)
    data = model_to_dict(payload)

    updated_task = task.model_copy(update=data) if hasattr(task, "model_copy") else task.copy(update=data)
    index = tasks.index(task)
    tasks[index] = updated_task
    return updated_task
