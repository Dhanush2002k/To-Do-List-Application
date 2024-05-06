class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index]['completed'] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{i+1}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            if todo_list.tasks:
                index = int(input("Enter index of task to delete: ")) - 1
                todo_list.delete_task(index)
            else:
                print("No tasks in the list.")
        elif choice == '3':
            if todo_list.tasks:
                index = int(input("Enter index of task to mark as completed: ")) - 1
                todo_list.mark_completed(index)
            else:
                print("No tasks in the list.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
