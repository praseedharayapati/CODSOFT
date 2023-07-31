import os
from colorama import Fore, Style


TASKS_FILE = "tasks.txt"

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Current tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(task, tasks):
    if task not in tasks:
        tasks.append(task)
        print(Fore.GREEN + "Task added successfully!" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Task already exists!" + Style.RESET_ALL)

def update_task(task_index, updated_task, tasks):
    if task_index < 1 or task_index > len(tasks):
        print(Fore.RED + "Invalid task index!" + Style.RESET_ALL)
    else:
        tasks[task_index - 1] = updated_task
        print(Fore.GREEN + "Task updated successfully!" + Style.RESET_ALL)

def remove_task(task_index, tasks):
    if task_index < 1 or task_index > len(tasks):
        print(Fore.RED + "Invalid task index!" + Style.RESET_ALL)
    else:
        removed_task = tasks.pop(task_index - 1)
        print(Fore.GREEN + f"Task '{removed_task}' removed successfully!" + Style.RESET_ALL)

def save_tasks_to_file(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def main():
    tasks = load_tasks_from_file()

    while True:
        print("\nChoose an option:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the new task: ")
            add_task(task, tasks)
            save_tasks_to_file(tasks)
        elif choice == "3":
            task_index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ")
            update_task(task_index, updated_task, tasks)
            save_tasks_to_file(tasks)
        elif choice == "4":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(task_index, tasks)
            save_tasks_to_file(tasks)
        elif choice == "5":
            print("Have A Good Day. Bye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Please choose again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
