# ✅ To-Do List App - Day 2
# This app lets you view tasks, add new ones, and saves/loads them from a file

# FILE NAME WHERE TASK WILL BE STORED
FILE_NAME = "tasks.txt"

#Create an empty list to hold task in memory
tasks = []

# Load tasks from the file

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("No existing task file found. Starting fresh.")

# Save tasks to the file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully.")

# Show the menu options
def show_menu():
    print("\n📋 TO-DO LIST")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# main program logic starts here
load_tasks()

# main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task added: {task}")
        save_tasks()
    elif choice == "3":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")