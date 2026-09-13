# MyTracker Data Models

## Task Model
- name: string (required)
- description: string (optional)
- priority: enum (low, medium, high) (default: medium)
- due_datetime: datetime (optional)
- completed: boolean (default: false)
- recurring_schedule: enum (none, daily, weekly, monthly, yearly) (default: none)
- recurring_end_condition: enum (never, after_n_occurrences, on_specific_date) (default: never)

## Goal Model
- name: string (required)
- description: string (optional)
- priority: enum (low, medium, high) (default: medium)
- due_date: datetime (optional)
- tasks: list of Task IDs (required)

## Journal Entry Model
- title: string (required)
- content: string (required)
- associated_tasks: list of Task IDs (optional)
- associated_goals: list of Goal IDs (optional)
- timestamp: datetime (automatically set at creation)

## Relationships
- Goals consist of one or more tasks
- Tasks can be associated with multiple goals
- Journal entries can be associated with multiple tasks and goals
- Goal completion is calculated from associated completed tasksOO