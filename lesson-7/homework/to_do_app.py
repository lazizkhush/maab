from abc import ABC, abstractmethod
import json
import csv

class StoreStrategy(ABC):
    @abstractmethod
    def load_tasks(self):
        pass
    @abstractmethod
    def save_tasks(self):
        pass


class JsonStorage(StoreStrategy):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def save_tasks(self, tasks):
        with open(self.filename, 'w') as f:
            return json.dump(tasks, f, indent=4)
        
class CsvStorage(StoreStrategy):
    def __init__(self, filename='tasks.csv'):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                read = csv.DictReader(f)
                return list(read)
        except FileNotFoundError:
            return[]
        
    def save_tasks(self, tasks):
        with open('tasks.csv', 'w', newline='') as f:
            fields = ['task_id', 'title', 'desc', 'due_date', 'status']
            writer = csv.DictWriter(f, fieldnames=fields)
        
            writer.writeheader()
            writer.writerows(tasks)


class ToDoApp:
    def __init__(self, storage: StoreStrategy):
        self.storage = storage
        self.tasks = self.storage.load_tasks()
        print("""Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")

    def add_task(self):
        task = {}
        task['task_id'] = input('Enter task ID: ')
        task["title"] = input('Enter task title: ')
        task["desc"] = input("Enter Description: ")
        due_date = input('Enter due data (Optional) (YYYY-MM-DD): ')
        task["due_date"] = due_date if due_date else "" 
        task['status'] = input('Enter status Pending/In Progress/Completed: ').title()
        self.tasks.append(task)
        
    
    def view_tasks(self):
        for task in self.tasks:
            for k, v in task.items():
                print(v+', ', end=' ')
            print()

    def update_task(self):
        task_id = input("Enter task ID: ")
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["title"] = input('Enter task title: ')
                task["desc"] = input("Enter Description: ")
                new_due_date = input(f'Enter new due date (YYYY-MM-DD) (press Enter to keep {task["due_date"]}): ').strip()
                task["due_date"] = new_due_date if new_due_date else task["due_date"]
                task['status'] = input('Enter status Pending/In Progress/Completed: ').title()
        
                
    def delete_task(self):
        task_id = input("Enter task ID: ")
        self.tasks = [task for task in self.tasks if task['task_id']!=task_id]

    def filter_tasks(self):
        filter_by = input('By what status you want to filter by: (Pending/In Progress/Completed)').title()
        filtered_tasks = [task for task in self.tasks if task['status']==filter_by]
        if not filtered_tasks:
            print(f'There are not any tasks with status {filter_by}')
        else:
            for task in filtered_tasks:
                for k, v in task.items():
                    print(v+', ', end=' ')
            print()


def save_tasks_to_storage(todo_app: ToDoApp):
    todo_app.storage.save_tasks(todo_app.tasks)
    print("Tasks saved successfully.")


def load_tasks_from_storage(todo_app: ToDoApp):
    todo_app.tasks = todo_app.storage.load_tasks()
    print("Tasks loaded successfully.")

storage = CsvStorage()     
todo = ToDoApp(storage)
while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.update_task()
    elif choice == "4":
        todo.delete_task()
    elif choice == "5":
        todo.filter_tasks()
    elif choice == "6":
        save_tasks_to_storage(todo)
    elif choice == "7":
        load_tasks_from_storage(todo)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

