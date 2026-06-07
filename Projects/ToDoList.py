#Making a TO DO list with options to add, view, clear, and exit.:a
def to_do_list():
    tasks = []
    while True:
        status = input("What Do You Want To Do? (add/view/clear/exit): ")
        if status.lower() == 'exit':
            break
        elif status.lower() == 'add':
            task = input("Enter a task to add to the To Do list (or 'done' to finish): ")
            tasks.append(task)
        elif status.lower() == 'view':
            print("To Do List:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
        elif status.lower() == 'clear':
            tasks.clear()
            print("To Do list cleared.")
        else:
            print("Invalid input. Please enter 'add', 'view', 'clear', or 'exit'.")
    return tasks

if __name__ == "__main__":
    to_do_list()