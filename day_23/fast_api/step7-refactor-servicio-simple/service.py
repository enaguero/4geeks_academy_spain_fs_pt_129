from typing import List, Optional

from fastapi import HTTPException, status

import repository
from schemas import Task, TaskCreate, TaskUpdate


def list_tasks(done: Optional[bool] = None) -> List[Task]:
    tasks = repository.list_tasks()
    if done is None:
        return tasks
    return [task for task in tasks if task.done == done]


def create_task(payload: TaskCreate) -> Task:
    duplicated = any(task.title.lower() == payload.title.lower() for task in repository.list_tasks())
    if duplicated:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe una tarea con ese titulo")

    task = Task(id=repository.next_task_id(), title=payload.title, done=False)
    return repository.save_task(task)


def update_task(task_id: int, payload: TaskUpdate) -> Task:
    task = repository.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")

    data = payload.model_dump(exclude_none=True) if hasattr(payload, "model_dump") else payload.dict(exclude_none=True)
    updated_task = task.model_copy(update=data) if hasattr(task, "model_copy") else task.copy(update=data)
    return repository.replace_task(task_id, updated_task)


def delete_task(task_id: int) -> None:
    deleted = repository.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
