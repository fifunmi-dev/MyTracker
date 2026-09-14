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
    cursor.execute("DELETE FROM goals WHERE title = ?", (test_goal.title,))
    db_manager.connection.commit()
    db_manager.disconnect()

def test_get_all_tasks():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()

    # Create a test task
    test_task = Task(
        title="Test Task for Retrieval",
        description="This is a test task for retrieval.",
        completed=False,
        priority=Priority.LOW,
        due_datetime=datetime.datetime(2024, 8, 1),
        recurring_schedule=RecurringSchedule.NONE,
        recurring_end_condition=RecurringEndCondition.NONE
    )

    # Insert the test task into the database
    db_manager.create_task(test_task)

    # Retrieve all tasks from the database
    tasks = db_manager.get_all_tasks()

    # Verify that the retrieved tasks include the test task
    assert any(task.title == test_task.title for task in tasks), "Test task was not retrieved from the database."
    # Clean up: delete the test task and disconnect from the database
    cursor = db_manager.connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE title = ?", (test_task.title,))
    db_manager.connection.commit()
    db_manager.disconnect()

def test_delete_task():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()
    # Create a test task
    test_task = Task(
        title="Test Task for Deletion",
        description="This is a test task for deletion.",
        completed=False,
        priority=Priority.MEDIUM,
        due_datetime=datetime.datetime(2024, 9, 1),
        recurring_schedule=RecurringSchedule.NONE,
        recurring_end_condition=RecurringEndCondition.NONE
    )
    # Insert the test task into the database
    db_manager.create_task(test_task)

    #Get ID of the test task
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT id FROM tasks WHERE title = ?", (test_task.title,))
    result = cursor.fetchone()
    test_task.id = result[0] if result else None

    # Delete the test task from the database
    db_manager.delete_task(test_task.id)
    # Verify that the task was deleted correctly
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (test_task.id,))
    result = cursor.fetchone()
    assert result is None, "Task was not deleted from the database."
    # Disconnect from the database
    db_manager.disconnect()

def test_edit_task():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()
    # Create a test task
    test_task = Task(
        title="Test Task for Editing",
        description="This is a test task for editing.",
        completed=False,
        priority=Priority.LOW,
        due_datetime=datetime.datetime(2024, 10, 1),
        recurring_schedule=RecurringSchedule.NONE,
        recurring_end_condition=RecurringEndCondition.NONE
    )
    # Insert the test task into the database
    db_manager.create_task(test_task)
    # Edit the test task's title and description
    new_title = "Edited Test Task"
    new_description = "This is an edited test task."

    #Edit the task object to reflect the changes
    test_task.title = new_title
    test_task.description = new_description

    db_manager.edit_task(test_task)
    # Verify that the task was edited correctly
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE title = ?", (new_title,))
    result = cursor.fetchone()
    assert result is not None, "Task was not found after editing."
    assert result[1] == new_title, "Task title was not updated correctly."
    assert result[2] == new_description, "Task description was not updated correctly."
    # Clean up: delete the edited task and disconnect from the database
    cursor.execute("DELETE FROM tasks WHERE title = ?", (new_title,))
    db_manager.connection.commit()
    db_manager.disconnect()

def test_complete_task():
    # Create a test database manager
    db_manager = DatabaseManager("test_database.db")
    db_manager.connect()
    db_manager.initialise_database()
    # Create a test task
    test_task = Task(
        title="Test Task for Completion",
        description="This is a test task for completion.",
        completed=False,
        priority=Priority.HIGH,
        due_datetime=datetime.datetime(2024, 11, 1),
        recurring_schedule=RecurringSchedule.NONE,
        recurring_end_condition=RecurringEndCondition.NONE
    )
    # Insert the test task into the database
    db_manager.create_task(test_task)
    # Complete the test task
    db_manager.complete_task(test_task.id)
    # Verify that the task was marked as completed correctly
    cursor = db_manager.connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (test_task.id,))
    result = cursor.fetchone()
    assert result is not None, "Task was not found after marking as completed."
    assert result[3] == 1, "Task was not marked as completed correctly."
    # Clean up: delete the completed task and disconnect from the database
    cursor.execute("DELETE FROM tasks WHERE id = ?", (test_task.id,))
    db_manager.connection.commit()
    db_manager.disconnect()