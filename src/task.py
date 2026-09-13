# Task class
from enum import Enum
import datetime

class Priority(Enum):
    LOW = "low" 
    MEDIUM = "medium"
    HIGH = "high"

class RecurringSchedule(Enum):
    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class RecurringEndCondition(Enum):
    NEVER = "never"
    AFTER_N_OCCURRENCES = "after_n_occurrences"
    ON_DATE = "on_date"


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
