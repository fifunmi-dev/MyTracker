# Task class
import datetime
from enums import Priority, RecurringSchedule, RecurringEndCondition

class Task:
    def __init__(self,
        name: str, 
        description: str = "", 
        completed: bool = False, 
        priority: Priority = Priority.MEDIUM,
        due_datetime: datetime.datetime = None,
        recurring_schedule: RecurringSchedule = RecurringSchedule.NONE,
        recurring_end_condition: RecurringEndCondition = RecurringEndCondition.NEVER
        ):

        self.__name = name
        self.__description = description
        self.__completed = completed
        self.__priority = priority
        self.__due_datetime = due_datetime
        self.__recurring_schedule = recurring_schedule
        self.__recurring_end_condition = recurring_end_condition
