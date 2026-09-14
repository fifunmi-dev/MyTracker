# Task class
import datetime
from .enums import Priority, RecurringSchedule, RecurringEndCondition

class Task:
    def __init__(self,
        title: str, 
        description: str = "", 
        completed: bool = False, 
        priority: Priority = Priority.MEDIUM,
        due_datetime: datetime.datetime = None,
        recurring_schedule: RecurringSchedule = RecurringSchedule.NONE,
        recurring_end_condition: RecurringEndCondition = RecurringEndCondition.NEVER
        ):

        self.id: int = None
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority
        self.due_datetime = due_datetime
        self.recurring_schedule = recurring_schedule
        self.recurring_end_condition = recurring_end_condition
