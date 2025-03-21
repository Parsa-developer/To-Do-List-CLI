import os
from colorama import Fore, Style, init

init(autoreset=True)
TODO_FILE = "task.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return [line.strip() for line in f.readline()]
    
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        f.write("\n".join(tasks))

def add_task(tasks):
    task = input(Fore.CYAN + "Enter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(Fore.GREEN + "✓ Task added!")
    else:
        print(Fore.RED + "✗ Task cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks Found!")
    else:
        print(Fore.BLUE + "\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(Fore.YELLOW + f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input(Fore.CYAN + "Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.MAGENTA + f"🗑 Removed: {removed}")
        else:
            print(Fore.RED + "✗ Invalid task number!")
    except ValueError:
        print(Fore.RED + "✗ Please enter a valid number!")



def main():
    tasks = load_tasks()
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n==== To-Do List ====")
        print(Fore.WHITE + "1. Add Task")
        print(Fore.WHITE + "2. Delete Task")
        print(Fore.WHITE + "3. View Tasks")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.CYAN + "\nChoose an option ( 1 - 4 ): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print(Fore.BLUE + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "✗ Invalid choice! Please pick ( 1 - 4 )")

if __name__ == '__main__':
    main()