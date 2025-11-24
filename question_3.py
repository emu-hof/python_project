# To-Do List App

def display_menu():
    print("\n*** TO-DO LIST MENU ***")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")

def add_task(tasks):
    title = input("Enter task name: ").strip()

    while True:
        priority = input("Enter priority (high/medium/low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Invalid priority! Please enter high, medium, or low.")

    tasks.append({"title": title, "priority": priority, "completed": False})
    print(f"Task '{title}' added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']} (Priority: {task['priority']}) => {status}")

def mark_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):   
                tasks[task_number - 1]["completed"] = True
                print(f"'{tasks[task_number - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(tasks):  
                removed = tasks.pop(task_number - 1)
                print(f"'{removed['title']}' deleted successfully.")
            else:
                print("Invalid task number. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_summary(tasks):
    completed = sum(task["completed"] for task in tasks)
    pending = len(tasks) - completed
    print("\n*** SUMMARY ***")
    print(f"Completed Tasks: {completed}")
    print(f"Pending Tasks: {pending}")
    print("Keep going!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5" or choice.lower() == "exit":
            show_summary(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
