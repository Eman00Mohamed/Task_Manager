'''

Task Manager System
This program:
- adds new tasks
- displays tasks
- updates existing tasks
- deletes tasks
- marks tasks as completed

'''

import json
from pathlib import Path

tasks = []

# Resolve the data file relative to this script's own location (not the
# current working directory), and keep it inside a dedicated data/ folder.
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DEFAULT_TASKS_FILE = DATA_DIR / "tasks.json"


def load_tasks(tasks, filename=DEFAULT_TASKS_FILE):
    try:
        with open(filename, "r") as file:
            tasks.extend(json.load(file))
    except json.JSONDecodeError:
        print("Error: The tasks file is corrupted. Starting with an empty task list.")
    except FileNotFoundError:
        print("No existing tasks file found. Starting with an empty task list.")


def save_tasks(tasks, filename=DEFAULT_TASKS_FILE):
    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError as e:
        print(f"Error: Could not save tasks to '{filename}'. {e}")

def add_task(tasks):
    title = input("Enter the task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    tasks.append({"id": new_id, "title": title, "is_completed": False})
    print(f"Task '{title}' added successfully.")
    save_tasks(tasks)



def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Completed" if task["is_completed"] else "Pending"
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def get_task_id():
    try:
        task_id = int(input("Enter task ID: "))
        return task_id
    except ValueError:
        print("Invalid task ID. Please enter a valid number.")
        return None

def update_task(tasks):
    task_id = get_task_id()
    if task_id is None:
        return None
    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Error: Task title cannot be empty.")
                return None
            task["title"] = new_title
            print(f"Task ID {task_id} updated successfully.")
            save_tasks(tasks)
            return task
    print("Task not found.")
    return None


def delete_task(tasks):
    task_id = get_task_id()
    if task_id is None:
        return False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully.")
            save_tasks(tasks)
            return True
    print("Task not found.")
    return False


def complete_task(tasks):
    task_id = get_task_id()
    if task_id is None:
        return False
    for task in tasks:
        if task["id"] == task_id:
            if task["is_completed"]:
                print(f"Task ID {task_id} is already completed.")
                return False
            task["is_completed"] = True
            print(f"Task ID {task_id} marked as completed.")
            save_tasks(tasks)
            return True
    print("Task not found.")
    return False

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


def main():
    load_tasks(tasks)  # Load tasks from file at the start of the program

    running = True
    while running:
        display_menu()
        try:
            user_choice = int(input("Enter your choice as a number: "))
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue
        match user_choice:
            case 1:
                add_task(tasks)
            case 2:
                view_tasks(tasks)
            case 3:
                update_task(tasks)
            case 4:
                delete_task(tasks)
            case 5:
                complete_task(tasks)
            case 6:
                running = False
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()