import sqlite3
from .. import Task, Goal

class DatabaseManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to database: {self.db_name}")

        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from database: {self.db_name}")

    def initialise_database(self):
        cursor = self.connection.cursor()
        
        #Create the tasks table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed INTEGER DEFAULT 0,
                priority TEXT NOT NULL,
                due_datetime TEXT,
                recurring_schedule TEXT NOT NULL,
                recurring_end_condition TEXT NOT NULL
            )
        ''')

        #Create the goals table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT NOT NULL,
                due_datetime TEXT,
                completed INTEGER DEFAULT 0
            )
        ''')

        #Create the goal_tasks table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS goal_tasks (
                id INTEGER PRIMARY KEY,
                goal_id INTEGER NOT NULL,
                task_id INTEGER NOT NULL,
                FOREIGN KEY (goal_id) REFERENCES goals (id),
                FOREIGN KEY (task_id) REFERENCES tasks (id)
            )
        ''')

    def create_task(self, task: Task):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, priority, due_date, recurring_schedule, recurring_end_condition, completed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (task.title, task.description, task.priority.value, str(task.due_datetime), task.recurring_schedule.value, task.recurring_end_condition.value, int(task.completed)))
        self.connection.commit()

    def create_goal(self, goal: Goal):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO goals (title, description, priority, due_date, completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (goal.title, goal.description, goal.priority.value, str(goal.due_datetime), int(goal.completed)))
        self.connection.commit()
