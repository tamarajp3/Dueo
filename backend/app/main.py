from fastapi import FastAPI
from core import Task
from scheduler import optimal_schedule
from pydantic import BaseModel
from models import createTask, scheduleRequest


app = FastAPI()

tasks = []

@app.get("/tasks")
def get_tasks():
    return [
        {
            "task_name": task.task_name,
            "time_left": task.time_left,
            "subject": task.subject
            } 
        for task in tasks
    ]

@app.post("/tasks")
def create_task(task : createTask):
    new = Task(
        task.task_name,
        task.assessment_type_multiplier,
        task.deadline,
        task.weighing,
        task.subject,
        task.estimated_time
    )
    tasks.append(new)

@app.post("/schedule")
def get_schedule(request: scheduleRequest):
    return optimal_schedule(tasks, request.daily_availability)

    