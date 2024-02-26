import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({'title': title, 'completed': False})
    print("Task added successfully.")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        tasks[index]['completed'] = True
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting program. Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
