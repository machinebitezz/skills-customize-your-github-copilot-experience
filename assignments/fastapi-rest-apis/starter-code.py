from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="School Tasks API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: list[Task] = [
    Task(
        id=1,
        title="Read the FastAPI documentation",
        description="Learn how path operations are declared.",
    )
]


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message for the API."""
    return {"message": "Welcome to the School Tasks API"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    """Return every task."""
    return tasks


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    """Create and return a new task."""
    next_id = max((task.id for task in tasks), default=0) + 1
    task = Task(id=next_id, **task_data.model_dump())
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    """Return one task by its ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate) -> Task:
    """Replace the editable fields of an existing task."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task_id, **task_data.model_dump(), completed=task.completed)
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    """Delete a task by its ID."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
