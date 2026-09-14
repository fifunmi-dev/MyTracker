from enum import Enum

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
    NONE = "none"
    NEVER = "never"
    AFTER_N_OCCURRENCES = "after_n_occurrences"
    ON_DATE = "on_date"
