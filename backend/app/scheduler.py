from core import Task
import collections

MAX_SUBJECT_STUDY_TIME = 3
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def optimal_schedule(tasks, daily_availability):

    tasks = sorted(tasks, key = lambda t:t.priority(), reverse = True)

    week_schedule = {
        day: {
            tasks: []
            total_task_time: 0,
            remaining_time: hours_per_day
        } for day in DAYS
    }

    for task in tasks:
        for day in daily_availabilty:
            day_data = week_schedule[day]

            if (task.estimated_time <= day_data[remaining_time]):
                day_data[tasks].append(task)
                day_data[total_task_time] += task.estimated_time
                day_data[remaining_time] -= task.estimated_time
                
    return week_schedule
    