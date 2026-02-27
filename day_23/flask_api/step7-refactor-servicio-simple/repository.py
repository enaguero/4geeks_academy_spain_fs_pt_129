from typing import List, Optional

from schemas import Task

_tasks: List[Task] = [
    Task(id=1, title="Repasar status codes", done=False),
    Task(id=2, title="Probar endpoint con checks.http", done=True),
]


def list_tasks() -> List[Task]:
    return _tasks


def get_task(task_id: int) -> Optional[Task]:
    for task in _tasks:
        if task.id == task_id:
            return task
    return None


def next_task_id() -> int:
    return max((task.id for task in _tasks), default=0) + 1


def save_task(task: Task) -> Task:
    _tasks.append(task)
    return task


def replace_task(task_id: int, updated_task: Task) -> Task:
    for index, task in enumerate(_tasks):
        if task.id == task_id:
            _tasks[index] = updated_task
            return updated_task
    raise ValueError("Task no encontrada")


def delete_task(task_id: int) -> bool:
    task = get_task(task_id)
    if task is None:
        return False
    _tasks.remove(task)
    return True
