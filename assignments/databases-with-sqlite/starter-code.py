# Starter Code: Databases with SQLite

import sqlite3

DATABASE_NAME = "tasks.db"

SAMPLE_TASKS = [
    ("Finish Python homework", "High", 0),
    ("Review class notes", "Medium", 0),
    ("Pack backpack", "Low", 1),
]


def connect_db():
    """Return a connection to the SQLite database."""
    # Task 1: Connect to tasks.db and return the connection.
    pass


def create_table(connection):
    """Create the tasks table if it does not already exist."""
    # Task 1: Create a table with id, title, priority, and completed columns.
    pass


def seed_tasks(connection):
    """Insert starter rows into the tasks table."""
    # Task 1: Insert SAMPLE_TASKS into the database.
    pass


def list_tasks(connection):
    """Print every task in the database."""
    # Task 2: Query all tasks and print each row.
    pass


def list_high_priority_tasks(connection):
    """Print only tasks with High priority."""
    # Task 2: Query only High priority tasks and print each row.
    pass


def complete_task(connection, task_id):
    """Mark one task as completed."""
    # Task 2: Update the matching task so completed = 1.
    pass


def main():
    connection = connect_db()

    create_table(connection)
    seed_tasks(connection)

    print("All tasks:")
    list_tasks(connection)

    print("\nHigh priority tasks:")
    list_high_priority_tasks(connection)

    print("\nMarking task 1 as completed...\n")
    complete_task(connection, 1)

    print("Updated tasks:")
    list_tasks(connection)

    connection.close()


if __name__ == "__main__":
    main()