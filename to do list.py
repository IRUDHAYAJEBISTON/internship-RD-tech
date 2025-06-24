todo_list = []

def show_menu():
    print("\nTo-Do List")
    print("1. See tasks")
    print("2. Add a task")
    print("3. Mark task done")
    print("4. Delete a task")
    print("5. Quit")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks right now.")
    else:
        print("\nTasks:")
        for i, task in enumerate(todo_list, 1):
            done = "Done" if task['completed'] else "Not done"
            print(f"{i}. {task['title']} - {done}")

def add_task():
    task = input("What do you want to add? ")
    todo_list.append({'title': task, 'completed': False})
    print("Added!")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Which task number did you finish? "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]['completed'] = True
            print("Marked as done.")
        else:
            print("That number doesn’t match any task.")
    except:
        print("Please enter a number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Which one do you want to delete? "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Removed '{removed['title']}'")
        else:
            print("No task with that number.")
    except:
        print("Give me a number please.")

def run_todo_app():
    print("Welcome to your To-Do List!")
    while True:
        show_menu()
        choice = input("Pick a number (1-5): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("See ya!")
            break
        else:
            print("Not a valid option, try again.")

run_todo_app()
