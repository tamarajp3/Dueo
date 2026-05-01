from core import Task
import collections

MAX_SUBJECT_STUDY_TIME = 3
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def optimal_schedule(tasks, hours_per_day):
    current_day_tasks = []

    tasks = sorted(tasks, key = lambda t:t.priority(), reverse = True)

    week_schedule = {
        day: {
            "tasks": []
            "total_task_time": 0,
            "remaining_time" = hours_per_day
        } for day in DAYS
    }

    for day in DAYS:
        day_stats = week_schedule[day]

        if (day_stats["total_task_time"] < hours_per_day)
    