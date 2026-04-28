from datetime import datetime

class Task:
    def __init__(self, task_name, assessment_type, deadline, weighing, subject, estimated_time="average", days_until_deadline):
        self.task_name = task_name
        self.assessment_type = assessment_type #quiz, project, content
        self.deadline = deadline #days until due
        self.days_until_deadline = None
        self.weighing = weighing
        self.subject = subject #class/subject
        self.estimated_time = estimated_time #optional field
    

    def days_until_deadline(self):
        time_now = datetime.now()

        return self.deadline - time_now
        

