from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task model
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory DB
tasks: List[Task] = []

@app.get("/")
def home():
    return {"message": "Welcome to To-Do API"}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted = tasks.pop(i)
            return {"message": "Task deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")
