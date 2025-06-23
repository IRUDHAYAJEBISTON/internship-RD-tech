todo_list = []

def show_menu():
    print("\n📋 To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({'title': title, 'completed': False})
    print("Task added successfully!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted = todo_list.pop(task_num - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def run_todo_app():
    print("📝 Welcome to the To-Do List App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
run_todo_app()
