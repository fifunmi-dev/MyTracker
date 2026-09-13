#Goal Class

from enums import Priority
import datetime


class Goal:
    def __init__(self,
                 name: str,
                 description: str = "",
                 priority: Priority = Priority.MEDIUM,
                 completed: bool = False,
                 due_datetime: datetime.datetime = None,
                 associated_tasks: list = None
                 ):

        self.__name = name
        self.__description = description
        self.__priority = priority
        self.__completed = completed
        self.__due_datetime = due_datetime
        self.__associated_tasks = associated_tasks if associated_tasks is not None else []
