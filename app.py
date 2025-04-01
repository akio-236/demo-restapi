from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


class BaseTodo(BaseModel):
    task: str


class Todo(BaseTodo):
    id: Optional[int] = None
    task: str
    completed: bool = False


class ReturntoTodo(BaseTodo):
    pass


app = FastAPI()

todos = []


@app.post("/todos", response_model=ReturntoTodo)
async def add_todos(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


@app.get("/todos")
async def read_todos(completed: Optional[bool] = None):
    if completed is None:
        return todos
    else:
        return [todo for todo in todos if todo.completed == completed]


@app.get("/todos/{id}")
async def read_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{id}")
async def update_todo(id: int, new_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = new_todo
            todos[index].id = id
            return new_todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            del todos[index]
            return
    raise HTTPException(status_code=404, detail="Todo not found")
