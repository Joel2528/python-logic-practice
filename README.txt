📚 Object-Oriented Programming (OOP) Projects
A collection of Python projects demonstrating core OOP principles: encapsulation, abstraction, inheritance, and polymorphism.
🎯 Projects Overview
1. 📋 Task Manager (task_manager_oop.py)
Main Project - A comprehensive task management system with clean separation of concerns.
Classes:

Task: Represents individual tasks with properties and behaviors

Properties: title, completed status, timestamps
Methods: mark_complete(), mark_incomplete(), get_details()


TaskManager: Manages a collection of tasks

Methods: add_task(), list_tasks(), mark_task_complete(), remove_task(), get_statistics()



Features:

✅ Add new tasks
📝 List all tasks or filter by status (pending/completed)
✔️ Mark tasks as complete/incomplete
🗑️ Remove individual tasks
🧹 Clear all completed tasks
📊 View statistics (total, completed, pending, completion rate)
⏰ Automatic timestamp tracking

OOP Principles Demonstrated:

Encapsulation: Task properties and manager operations are well-contained
Abstraction: Clean public interfaces hide implementation details
Single Responsibility: Each class has one clear purpose
Type Hints: Full type annotations for better code quality


2. 🏦 Bank Account (bank_account.py)
Banking system demonstrating encapsulation and property management.
Features:

Create accounts with unique account numbers
Deposit and withdraw money
Transfer between accounts
View transaction history and statements
Automatic balance tracking

OOP Principles:

Encapsulation: Private balance attribute (_balance)
Properties: Read-only balance access via @property
Class Variables: Automatic account number generation
Validation: Input validation for all operations


3. 🎓 Student Management (student.py)
Student and classroom management system with grade tracking.
Classes:

Student: Individual student with grades
Classroom: Collection of students with analytics

Features:

Add/remove grades by subject
Calculate averages (per subject or overall)
Letter grade conversion (A-F)
Generate report cards
Classroom-level statistics
Top students ranking

OOP Principles:

Composition: Classroom contains multiple Students
Aggregation: Flexible student management
Methods: Rich behavior for both classes
Data Organization: Dictionary for subject-grade mapping


🚀 Getting Started
Prerequisites

Python 3.7 or higher
No external dependencies required (all using standard library)

Running the Projects
Task Manager (Interactive):
bashpython task_manager_oop.py
Bank Account (Demo):
bashpython bank_account.py
Student System (Demo):
bashpython student.py

📖 Usage Examples
Task Manager Example:
pythonfrom task_manager_oop import Task, TaskManager

# Create manager
manager = TaskManager()

# Add tasks
manager.add_task("Complete Python assignment")
manager.add_task("Read OOP chapter")
manager.add_task("Practice coding")

# Mark task complete
manager.mark_task_complete(0)

# Get statistics
stats = manager.get_statistics()
print(f"Completion rate: {stats['completion_rate']:.1f}%")
Bank Account Example:
pythonfrom bank_account import BankAccount

# Create accounts
alice = BankAccount("Alice Smith", 1000.0)
bob = BankAccount("Bob Johnson", 500.0)

# Perform operations
alice.deposit(200)
alice.withdraw(150)
alice.transfer(bob, 100)

# View statement
alice.get_statement()
Student Example:
pythonfrom student import Student, Classroom

# Create student
student = Student("Alice Johnson", 20)

# Add grades
student.add_grade("Mathematics", 95)
student.add_grade("Programming", 88)

# Get average
avg = student.get_average()
print(f"Average: {avg:.1f}")

# Generate report card
student.get_report_card()

🏗️ Project Structure
oop/
├── task_manager_oop.py    # Main task manager (interactive CLI)
├── bank_account.py        # Banking system with demo
├── student.py             # Student management with demo
└── README.md              # This file

🎓 OOP Concepts Covered
1. Classes and Objects

Defining classes with __init__ constructors
Creating and using instances (objects)
Class vs instance variables

2. Encapsulation

Private attributes (using _ prefix convention)
Public interfaces via methods
Data hiding and controlled access

3. Properties

Using @property decorator for read-only access
Getters and setters
Computed properties

4. Methods

Instance methods (access instance data)
Private methods (implementation details)
Special methods (__str__, __repr__, __len__)

5. Type Hints

Function annotations
Return type specifications
Optional types for nullable values

6. Design Patterns

Single Responsibility Principle
Separation of concerns
Clean public APIs


💡 Key Learnings
Task Manager Project:

Separation of Concerns: Task class handles task data, TaskManager handles operations
User Experience: Clean menu system with validation and error handling
Statistics: Demonstrating computed properties and aggregation
Scalability: Easy to extend with new features

Bank Account Project:

Data Protection: Private balance can't be modified directly
Transaction Logging: Automatic history tracking
Class Variables: Shared state for account numbering
Validation: Preventing invalid operations

Student Project:

Composition: Classroom composed of Students
Data Structures: Using dictionaries for flexible grade storage
Calculations: Average computation and letter grade conversion
Sorting: Custom sorting for rankings


🔧 Customization Ideas
Task Manager:

Add task priority levels
Add due dates and reminders
Add task categories/tags
Implement task filtering and search
Add data persistence (save to file)

Bank Account:

Add interest calculation
Add account types (savings, checking)
Add transaction limits
Implement overdraft protection
Add monthly statements

Student:

Add weighted grades
Add attendance tracking
Add course enrollment system
Add GPA calculation
Add grade curves


📝 Testing the Code
Each file includes a demo function that can be run directly:
bash# Run all demos
python task_manager_oop.py  # Interactive
python bank_account.py      # Auto demo
python student.py           # Auto demo

🎯 Best Practices Demonstrated

Clear Naming: Descriptive class and method names
Documentation: Comprehensive docstrings
Type Hints: Full type annotations
Error Handling: Validation and informative messages
Formatting: Consistent code style
User Feedback: Clear success/error messages
Modularity: Reusable, independent classes


📚 Further Reading

Python OOP Documentation
Real Python - OOP
Python Type Hints


👨‍💻 Author Notes
These projects demonstrate clean OOP design with:

Clear class responsibilities
Well-defined interfaces
Proper encapsulation
Comprehensive error handling
User-friendly interaction

Perfect for learning OOP fundamentals and building more complex applications!

🎉 Conclusion
This project collection shows how OOP principles create:

Organized Code: Clear structure and responsibilities
Reusable Components: Classes can be imported and used elsewhere
Maintainable Systems: Easy to understand and modify
Scalable Solutions: Simple to extend with new features

Happy coding! 🚀