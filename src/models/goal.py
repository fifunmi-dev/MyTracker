#Goal Class

from enums import Priority
import datetime


class Goal:
    def __init__(self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        completed: bool = False,
        due_datetime: datetime.datetime = None,
        associated_task_ids: list[int] = []
        ):

        self.id: int = None
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.due_datetime = due_datetime
        self.associated_task_ids = associated_task_ids
