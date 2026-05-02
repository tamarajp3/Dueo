from core import Task
import collections

MAX_TASK_TIME_DAILY = 4
MAX_STUDY_TIME_DAILY = 16

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def optimal_schedule(tasks, daily_availability):

    tasks = sorted(tasks, key = lambda t:(t.get_time_until_deadline, t.priority()), reverse = True)

    week_schedule = {
        day: {
            "tasks": [],
            "total_task_time": 0,
            "remaining_time": daily_availability.get(day, 0)
        } for day in DAYS
    }

    for task in tasks:
        for day in DAYS:
            if (task.is_complete()):
                break

            day_data = week_schedule[day]

            chunk = min(
                MAX_TASK_TIME_DAILY,
                day_data["remaining_time"],
                task.time_left,
                (MAX_STUDY_TIME_DAILY - day_data["total_task_time"])
            )

            if (chunk > 0):
                day_data["tasks"].append({
                    "task_name": task.task_name,
                    "hours": chunk,
                    "subject": task.subject
                })
                day_data["total_task_time"] += chunk
                day_data["remaining_time"] -= chunk
                task.time_left -= chunk

    return week_schedule 
    