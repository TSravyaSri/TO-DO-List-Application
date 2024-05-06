class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Completed)"
            print("Task marked as completed!")
        else:
            print("Invalid task index")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index")

    def show_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter index of task to mark as completed: ")) - 1
            todo_list.complete_task(index)
        elif choice == "4":
            index = int(input("Enter index of task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    print("Welcome to the To-Do List Application!")
    print("Instructions:")
    print("- Enter the respective number to perform the desired action.")
    print("- Enjoy managing your tasks!\n")
    main()
