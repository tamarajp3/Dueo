from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class createTask(BaseModel):
    task_name: str 
    assessment_type_multiplier : float
    deadline : datetime
    weighing : float
    subject : str
    estimated_time : float


class scheduleRequest(BaseModel):
    daily_availability: dict