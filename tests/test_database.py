from models import DatabaseManager, Task, Goal, Priority, RecurringSchedule, RecurringEndCondition
import datetime

def test_create_task():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()
    # Create a test task
    test_task = Task(
        title="Test Task",
        description="This is a test task.",
        completed=False,
        priority=Priority.HIGH,
        due_datetime=datetime.datetime(2024, 6, 30),
        recurring_schedule=RecurringSchedule.NONE,
        recurring_end_condition=RecurringEndCondition.NONE
    )

    # Insert the test task into the database
    db_manager.create_task(test_task)

    # Verify that the task was inserted correctly
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE title = ?", (test_task.title,))
    result = cursor.fetchone()
    assert result is not None, "Task was not inserted into the database."
    assert result[1] == test_task.title, "Task title does not match."
    assert result[2] == test_task.description, "Task description does not match."
    assert result[3] == int(test_task.completed), "Task completed status does not match."
    assert result[4] == test_task.priority.value, "Task priority does not match."
    assert result[5] == str(test_task.due_datetime), "Task due datetime does not match."
    assert result[6] == test_task.recurring_schedule.value, "Task recurring schedule does not match."
    assert result[7] == test_task.recurring_end_condition.value, "Task recurring end condition does not match."

    # Clean up: delete the test task and disconnect from the database
    cursor.execute("DELETE FROM tasks WHERE title = ?", (test_task.title,))
    db_manager.connection.commit()
    db_manager.disconnect()

def test_create_goal():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()

    # Create a test goal
    test_goal = Goal(
        title="Test Goal",
        description="This is a test goal.",
        completed=False,
        priority=Priority.MEDIUM,
        due_datetime=datetime.datetime(2024, 7, 15)
    )

    # Insert the test goal into the database
    db_manager.create_goal(test_goal)
    
    # Verify that the goal was inserted correctly
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT * FROM goals WHERE title = ?", (test_goal.title,))
    result = cursor.fetchone()
    assert result is not None, "Goal was not inserted into the database."
    assert result[1] == test_goal.title, "Goal title does not match."
    assert result[2] == test_goal.description, "Goal description does not match."
    assert result[3] == test_goal.priority.value, "Goal priority does not match."
    assert result[4] == str(test_goal.due_datetime), "Goal due datetime does not match."
    assert result[5] == int(test_goal.completed), "Goal completed status does not match."
    
    # Clean up: delete the test goal and disconnect from the database
    #cursor.execute("DELETE FROM goals WHERE title = ?", (test_goal.title,))
    db_manager.connection.commit()
    db_manager.disconnect()

