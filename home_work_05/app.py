from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4

app = FastAPI()

# Модель задачи
class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: str
    completed: bool = False

# Хранилище задач
tasks = {}

# Получение списка всех задач
@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return list(tasks.values())

# Получение задачи по ID
@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: UUID):
    if task_id in tasks:
        return tasks[task_id]
    raise HTTPException(status_code=404, detail="Task not found")

# Добавление новой задачи
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    task.id = uuid4()
    tasks[task.id] = task
    return task

# Обновление задачи
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task_update: Task):
    if task_id in tasks:
        task = tasks[task_id]
        task.title = task_update.title
        task.description = task_update.description
        task.completed = task_update.completed
        tasks[task_id] = task
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Удаление задачи
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID):
    if task_id in tasks:
        del tasks[task_id]
        return
    raise HTTPException(status_code=404, detail="Task not found")
