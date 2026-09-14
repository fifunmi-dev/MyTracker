import sqlite3
from ..task import Task 
from ..goal import Goal
from ..enums import Priority, RecurringSchedule, RecurringEndCondition
import datetime

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
            INSERT INTO tasks (title, description, priority, due_datetime, recurring_schedule, recurring_end_condition, completed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (task.title, task.description, task.priority.value, str(task.due_datetime), task.recurring_schedule.value, task.recurring_end_condition.value, int(task.completed)))
        self.connection.commit()

        cursor.execute('SELECT last_insert_rowid()')
        task_id = cursor.fetchone()[0]
        task.id = task_id


    def get_all_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(
                title=row[1],
                description=row[2],
                priority=Priority(row[4]),
                due_datetime=datetime.datetime.fromisoformat(row[5]),
                recurring_schedule=RecurringSchedule(row[6]),
                recurring_end_condition=RecurringEndCondition(row[7]),
                completed=bool(row[3])
            )
            task.id = row[0]
            tasks.append(task)
        return tasks

    def delete_task(self, task_id: int):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.connection.commit()

    def edit_task(self, task: Task):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE tasks
            SET title = ?, description = ?, priority = ?, due_datetime = ?, recurring_schedule = ?, recurring_end_condition = ?, completed = ?
            WHERE id = ?
        ''', (task.title, task.description, task.priority.value, str(task.due_datetime), task.recurring_schedule.value, task.recurring_end_condition.value, int(task.completed), task.id))
        self.connection.commit()

    def complete_task(self, task_id: int):
        cursor = self.connection.cursor()
        cursor.execute('''
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
        ''', (task_id,))
        self.connection.commit()

    def create_goal(self, goal: Goal):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO goals (title, description, priority, due_datetime, completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (goal.title, goal.description, goal.priority.value, str(goal.due_datetime), int(goal.completed)))
        self.connection.commit()