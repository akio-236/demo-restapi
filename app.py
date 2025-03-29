from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    id: Optional[int] = None
    task: str
    completed: bool = False


app = FastAPI()

todos = []


@app.post("/todos")
async def add_todos(todo: Todo):
    todos.append(todo)
    return todo
