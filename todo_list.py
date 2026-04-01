TASKS_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        return

    print("\n📋 Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            task_number = int(input("Task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"🗑️ Removed: {removed}")
            else:
                print("❌ Invalid number.")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")


main()