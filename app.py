from fastapi import FastAPI

app = FastAPI()

todos = []


@app.post("/todos")
async def add_todos(data):
    todos.append(data)
    return data
