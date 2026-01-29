"""
Simple Task Manager Application
A command-line task management tool
"""

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_description):
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': task_description,
            'completed': False
        }
        self.tasks.append(task)
        return task
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return task
        return None
    
    def list_tasks(self):
        """List all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
    
    def remove_task(self, task_id):
        """Remove a task from the list"""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]


def main():
    """Main application entry point"""
    manager = TaskManager()
    
    print("Welcome to Task Manager!")
    print("Commands: add, list, complete, remove, exit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            description = input("Enter task description: ")
            manager.add_task(description)
            print("Task added successfully!")
        elif command == "list":
            manager.list_tasks()
        elif command == "complete":
            try:
                task_id = int(input("Enter task ID: "))
                if manager.complete_task(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid task ID!")
        elif command == "remove":
            try:
                task_id = int(input("Enter task ID: "))
                manager.remove_task(task_id)
                print("Task removed successfully!")
            except ValueError:
                print("Invalid task ID!")
        else:
            print("Unknown command. Try: add, list, complete, remove, exit")


if __name__ == "__main__":
    main()

