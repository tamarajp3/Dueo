from fastapi import FastAPI
from core import Task
from scheduler import optimal_schedule
from pydantic import BaseModel


app = FastAPI()

tasks = []

@app.get("/tasks"):
def get_tasks():
    return (t.taskname for t in tasks)

@app.post("/tasks"):
def create_task(task : createTask):
    new = Task(
        task.task_name
        task.assessment_type_multiplier
        task.deadline = datetime
        task.weighing = weighing
        task.estimated_time = estimated_time
    )
    tasks.append(new)

@app.post("/schedule"):
def get_schedule(request: scheduleRequest):
    return optimal_schedule(tasks, request.hours_per_day)

    