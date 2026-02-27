from typing import List, Optional

from fastapi import FastAPI, Response, status

import service
from schemas import Task, TaskCreate, TaskUpdate

app = FastAPI(title="Step 7 - Refactor por capas")


@app.get("/tasks", response_model=List[Task])
def list_tasks(done: Optional[bool] = None):
    return service.list_tasks(done)


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    return service.create_task(payload)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    return service.update_task(task_id, payload)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    service.delete_task(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
