tasks = []

def add_task():
    task = input("Enter your task here : ")
    tasks.append({"task": task, "Done": False})

def view_task_list():
    i = 0
    while i < len(tasks):
        task = tasks[i]
        check = "✓" if task["Done"] else "x"
        print(f"{i + 1}. [{check}] {task['task']}")
        i += 1

def update_task():
    view_task_list()
    try:
        task_number = int(input("Enter task number you want to update (Done /not done): ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = not tasks[task_number]["completed"]
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def main():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task ")
        print("4. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task_list()
        elif choice == "3":
            update_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()