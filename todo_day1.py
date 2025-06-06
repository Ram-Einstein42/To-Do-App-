# ✅ To-Do List App - Day 1
# Features: Add tasks, view tasks

tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def view_tasks():
    if not task:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, t in enumerate(task, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task added: {task}")

# main loop
while True:
    show_menu()
    choice = input("> ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("Goodbye, Joy Boy!")
        break
    else:
        print("Invalid choice. Try again.")