# 📘 Assignment: Databases with SQLite

## 🎯 Objective

Practice storing and retrieving persistent data in Python with SQLite. You will create a small task tracker database, add records with SQL, and write queries that read and update saved data.

## 📝 Tasks

### 🛠️ Create the Database and Table

#### Description
Use Python's built-in `sqlite3` module to create a local database file for a task tracker. Build a `tasks` table and insert starter records so the program has data to work with.

#### Requirements
Completed program should:

- Create or connect to a SQLite database file named `tasks.db`.
- Create a `tasks` table with columns for `id`, `title`, `priority`, and `completed`.
- Insert at least 3 sample tasks into the table.
- Use `starter-code.py` as the main file for the assignment.


### 🛠️ Query and Update Task Data

#### Description
Write SQL queries that display saved tasks and update one task as completed. Show that the data changes persist by printing the task list before and after the update.

#### Requirements
Completed program should:

- Display all tasks from the database in a readable format.
- Display only the tasks with a priority of `High`.
- Update one task so its `completed` value changes from `0` to `1`.
- Print the updated task list to confirm the change was saved.