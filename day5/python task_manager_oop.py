"""
Task Manager - Object-Oriented Programming Implementation
A comprehensive task management system demonstrating OOP principles.
"""

from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single task with its properties and behaviors.
    
    Attributes:
        title (str): The title/description of the task
        completed (bool): Completion status of the task
        created_at (datetime): Timestamp when task was created
        completed_at (datetime): Timestamp when task was completed
    """
    
    def __init__(self, title: str):
        """
        Initialize a new Task.
        
        Args:
            title (str): The task description
        """
        self.title = title
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def mark_complete(self) -> None:
        """Mark the task as completed and record completion time."""
        if not self.completed:
            self.completed = True
            self.completed_at = datetime.now()
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None
    
    def __str__(self) -> str:
        """
        String representation of the task.
        
        Returns:
            str: Formatted task information
        """
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation of the task.
        
        Returns:
            str: Detailed task information
        """
        return f"Task(title='{self.title}', completed={self.completed})"
    
    def get_details(self) -> str:
        """
        Get detailed information about the task.
        
        Returns:
            str: Detailed task information including timestamps
        """
        status = "Completed" if self.completed else "Pending"
        details = f"{self}\n"
        details += f"  Status: {status}\n"
        details += f"  Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        if self.completed_at:
            details += f"  Completed: {self.completed_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        return details


class TaskManager:
    """
    Manages a collection of tasks with CRUD operations.
    
    Attributes:
        tasks (List[Task]): List of all tasks
    """
    
    def __init__(self):
        """Initialize an empty task manager."""
        self.tasks: List[Task] = []
    
    def add_task(self, title: str) -> Task:
        """
        Add a new task to the manager.
        
        Args:
            title (str): The task description
            
        Returns:
            Task: The newly created task
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(title.strip())
        self.tasks.append(task)
        return task
    
    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """
        Get all tasks, optionally filtering by completion status.
        
        Args:
            show_completed (bool): Whether to include completed tasks
            
        Returns:
            List[Task]: List of tasks matching the filter
        """
        if show_completed:
            return self.tasks
        else:
            return [task for task in self.tasks if not task.completed]
    
    def get_task(self, index: int) -> Optional[Task]:
        """
        Get a task by its index.
        
        Args:
            index (int): The task index (0-based)
            
        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None
    
    def mark_task_complete(self, index: int) -> bool:
        """
        Mark a task as complete by index.
        
        Args:
            index (int): The task index (0-based)
            
        Returns:
            bool: True if successful, False otherwise
        """
        task = self.get_task(index)
        if task:
            task.mark_complete()
            return True
        return False
    
    def mark_task_incomplete(self, index: int) -> bool:
        """
        Mark a task as incomplete by index.
        
        Args:
            index (int): The task index (0-based)
            
        Returns:
            bool: True if successful, False otherwise
        """
        task = self.get_task(index)
        if task:
            task.mark_incomplete()
            return True
        return False
    
    def remove_task(self, index: int) -> bool:
        """
        Remove a task by index.
        
        Args:
            index (int): The task index (0-based)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False
    
    def clear_completed(self) -> int:
        """
        Remove all completed tasks.
        
        Returns:
            int: Number of tasks removed
        """
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return initial_count - len(self.tasks)
    
    def get_statistics(self) -> dict:
        """
        Get task statistics.
        
        Returns:
            dict: Statistics including total, completed, and pending tasks
        """
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }
    
    def __len__(self) -> int:
        """Return the number of tasks."""
        return len(self.tasks)
    
    def __str__(self) -> str:
        """String representation of the task manager."""
        stats = self.get_statistics()
        return f"TaskManager({stats['total']} tasks, {stats['completed']} completed)"


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("📋 TASK MANAGER".center(50))
    print("="*50)
    print("1. Add Task")
    print("2. List All Tasks")
    print("3. List Pending Tasks")
    print("4. Mark Task Complete")
    print("5. Mark Task Incomplete")
    print("6. Remove Task")
    print("7. Clear Completed Tasks")
    print("8. Show Statistics")
    print("9. Exit")
    print("="*50)


def display_tasks(tasks: List[Task], title: str = "Tasks"):
    """
    Display a list of tasks with indices.
    
    Args:
        tasks (List[Task]): List of tasks to display
        title (str): Title for the task list
    """
    print(f"\n{title}:")
    print("-" * 50)
    
    if not tasks:
        print("  No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"  {i}. {task}")
    
    print("-" * 50)


def get_task_index(manager: TaskManager, prompt: str = "Enter task number: ") -> Optional[int]:
    """
    Get a valid task index from user input.
    
    Args:
        manager (TaskManager): The task manager instance
        prompt (str): Prompt to display
        
    Returns:
        Optional[int]: Valid index or None if invalid
    """
    try:
        index = int(input(prompt))
        if 0 <= index < len(manager):
            return index
        else:
            print(f"❌ Invalid task number. Please enter 0-{len(manager)-1}")
            return None
    except ValueError:
        print("❌ Please enter a valid number.")
        return None


def main():
    """Main application loop."""
    manager = TaskManager()
    
    print("🎉 Welcome to Task Manager!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            # Add Task
            title = input("Enter task description: ").strip()
            if title:
                try:
                    task = manager.add_task(title)
                    print(f"✅ Task added successfully: {task}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            else:
                print("❌ Task description cannot be empty.")
        
        elif choice == "2":
            # List All Tasks
            tasks = manager.list_tasks()
            display_tasks(tasks, "All Tasks")
        
        elif choice == "3":
            # List Pending Tasks
            tasks = manager.list_tasks(show_completed=False)
            display_tasks(tasks, "Pending Tasks")
        
        elif choice == "4":
            # Mark Task Complete
            if len(manager) == 0:
                print("❌ No tasks available.")
            else:
                display_tasks(manager.list_tasks())
                index = get_task_index(manager)
                if index is not None:
                    if manager.mark_task_complete(index):
                        print(f"✅ Task marked as complete!")
                    else:
                        print("❌ Failed to mark task as complete.")
        
        elif choice == "5":
            # Mark Task Incomplete
            if len(manager) == 0:
                print("❌ No tasks available.")
            else:
                display_tasks(manager.list_tasks())
                index = get_task_index(manager)
                if index is not None:
                    if manager.mark_task_incomplete(index):
                        print(f"✅ Task marked as incomplete!")
                    else:
                        print("❌ Failed to mark task as incomplete.")
        
        elif choice == "6":
            # Remove Task
            if len(manager) == 0:
                print("❌ No tasks available.")
            else:
                display_tasks(manager.list_tasks())
                index = get_task_index(manager)
                if index is not None:
                    task = manager.get_task(index)
                    if manager.remove_task(index):
                        print(f"✅ Task removed: {task}")
                    else:
                        print("❌ Failed to remove task.")
        
        elif choice == "7":
            # Clear Completed Tasks
            count = manager.clear_completed()
            print(f"✅ Removed {count} completed task(s).")
        
        elif choice == "8":
            # Show Statistics
            stats = manager.get_statistics()
            print("\n📊 Task Statistics:")
            print("-" * 50)
            print(f"  Total Tasks: {stats['total']}")
            print(f"  Completed: {stats['completed']}")
            print(f"  Pending: {stats['pending']}")
            print(f"  Completion Rate: {stats['completion_rate']:.1f}%")
            print("-" * 50)
        
        elif choice == "9":
            # Exit
            print("\n👋 Thank you for using Task Manager!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-9.")


if __name__ == "__main__":
    main()