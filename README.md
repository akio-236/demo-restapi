# demo-restapi
# FastAPI Todo Application

A simple Todo API built with FastAPI that allows you to create, read, update, and delete todo items with additional features like background tasks and middleware.

## Features

- Create, Read, Update, and Delete (CRUD) Todo items
- Filter todos by completion status
- Background task for sending email notifications (simulated)
- Request logging middleware
- CORS enabled for all origins
- Pydantic models for data validation

## API Endpoints

| Method | Endpoint       | Description                          | Request Body                              |
|--------|----------------|--------------------------------------|-------------------------------------------|
| POST   | /todos         | Create a new todo                    | `{"task": "string", "completed": bool}`   |
| GET    | /todos         | Get all todos (filter by completed)  | Query param: `?completed=true/false`      |
| GET    | /todos/{id}    | Get a specific todo by ID            | -                                         |
| PUT    | /todos/{id}    | Update a todo by ID                   | `{"task": "string", "completed": bool}`   |
| DELETE | /todos/{id}    | Delete a todo by ID                   | -                                         |

## Models

## **Todo**
```json
{
  "id": 1,
  "task": "string",
  "completed": false
}
```
# Todo creation
```json
{
  "task": "string"
}
```
## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/akio-236/fastapi-todo.git
   cd fastapi-todo
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```
# Running the application
**Start the server using uvicorn:**
```bash
uvicorn main:app --reload
```
# Testing the API
You can test the API using tools like:

- **FastAPI's built-in docs at http://127.0.0.1:8000/docs**
- **Postman**
- **cURL**
  
## Example cURL commands:

**Create a todo:**

```bash
curl -X POST "http://127.0.0.1:8000/todos" -H "Content-Type: application/json" -d '{"task":"Buy groceries"}'
```

**Get all todos:**
```bash
curl "http://127.0.0.1:8000/todos"
```
# API Documentation
![{C1C03CE2-8A28-4ABF-8353-877897946671}](https://github.com/user-attachments/assets/5bcc4bdf-2845-49b4-8a91-f6e73ca50038)



# Middleware
**The application included:**
- CORS middleware to allow cross-origin requests
- Logging middleware that tracks request processing time

# Background Tasks
When creating a new todo, a background task simulates sending an email notification.

# Dependencies
- **Python 3.7+**
- **FastAPI**
- **Uvicorn (ASGI server)**
- **Pydantic (included with FastAPI)**
  
