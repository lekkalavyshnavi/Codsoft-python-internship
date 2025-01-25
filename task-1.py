tasks = []

def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def add_task():
    task_name = input("\nEnter a new task: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added!")

def update_task():
    show_tasks()
    try:
        num = int(input("\nEnter the task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[num - 1]["task"] = new_task
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    show_tasks()
    try:
        num = int(input("\nEnter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_done():
    show_tasks()
    try:
        num = int(input("\nEnter the task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
