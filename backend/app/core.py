from datetime import datetime

class Task:
    def __init__(self, task_name, assessment_type_multiplier, deadline, weighing, subject, estimated_time):
        self.task_name = task_name
        self.assessment_type_multiplier  = assessment_type_multiplier # 0.5 = quiz, 2 = project, 0.25 = content
        self.deadline = datetime #datetime string
        self.weighing = weighing
        self.subject = subject #class/subject
        self.estimated_time = estimated_time
    
    def get_time_until_deadline(self):
        delta = self.deadline - datetime.now()
        return (delta.total_seconds()/86400)

    def priority(self):
        time_left = self.get_time_until_deadline()
        
        overdue_bias = 1
        if time_left < 0:
            overdue_bias = 1 + abs(time_left)

        safe_time = max(time_left, 0.1)

        task_urgency = 1 / safe_time
        task_importance = self.weighing * self.assessment_type_multiplier

        return task_importance * task_urgency * overdue_bias

    
