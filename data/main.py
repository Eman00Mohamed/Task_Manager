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

tasks = []

def load_tasks(tasks, filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks.extend(json.load(file))
    except json.JSONDecodeError:
        print("Error: The tasks file is corrupted. Starting with an empty task list.")
    except FileNotFoundError:
        print("No existing tasks file found. Starting with an empty task list.")


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"id": len(tasks) + 1, "title": title, "is_completed": False})
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
    new_title = input("Enter new title: ")
    for task in tasks:
        if task["id"] == task_id:
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
            # Reassign IDs to remaining tasks
            for index, task in enumerate(tasks):
                task["id"] = index + 1
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

