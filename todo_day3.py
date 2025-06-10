# ✅ To-Do List App - Day 3
# Features: Mark tasks complete using dictionary structure

import os

FILE_NAME = "tasks.txt"
tasks = []

# 🟩 Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as file:
        for line in file:
            # Split line into task text and done status
            parts = line.strip().split("||")
            if len(parts) == 2:
                task_text, done_status = parts
                tasks.append({"task": task_text, "done": done_status == "True"})

# 💾 Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            # Store each task as: task_text||True/False
            file.write(f"{task['task']}||{task['done']}\n")

# 🧾 Show the main menu
def show_menu():
    print("\n📋 TO-DO LIST")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task complete")
    print("4. Exit")

# 👁 View all tasks with done status
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {status} {task['task']}")

# ➕ Add new task
def add_task():
    task_text = input("Enter the task: ")
    tasks.append({"task": task_text, "done": False})
    save_tasks()
    print(f"✅ Task added: {task_text}")

# ☑ Mark a task as complete
def mark_complete():
    view_tasks()
    try:
        choice = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks()
            print("🎉 Task marked as complete!")
        else:
            print("⚠ Invalid number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

# 🌀 Main Program
load_tasks()

while True:
    show_menu()
    choice = input("> ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        print("Goodbye, Joy Boy!")
        break
    else:
        print("Invalid choice. Try again.")
