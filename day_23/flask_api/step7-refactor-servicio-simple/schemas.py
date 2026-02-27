from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=80)
    done: Optional[bool] = None
