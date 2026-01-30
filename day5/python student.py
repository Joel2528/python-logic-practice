"""
Student Management System - Demonstrating Classes and Methods
A system to manage student information and grades.
"""

from typing import Dict, List, Optional


class Student:
    """
    Represents a student with personal info and academic records.
    
    Attributes:
        student_id (str): Unique student identifier
        name (str): Student's full name
        age (int): Student's age
        grades (Dict[str, List[float]]): Grades organized by subject
    """
    
    # Class variable for student ID generation
    _next_id = 1
    
    def __init__(self, name: str, age: int):
        """
        Initialize a new student.
        
        Args:
            name (str): Student's full name
            age (int): Student's age
            
        Raises:
            ValueError: If age is not positive
        """
        if age <= 0:
            raise ValueError("Age must be positive")
        
        self.student_id = f"STU{Student._next_id:04d}"
        Student._next_id += 1
        
        self.name = name
        self.age = age
        self.grades: Dict[str, List[float]] = {}
    
    def add_grade(self, subject: str, grade: float) -> None:
        """
        Add a grade for a specific subject.
        
        Args:
            subject (str): The subject name
            grade (float): The grade (0-100)
            
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        
        if subject not in self.grades:
            self.grades[subject] = []
        
        self.grades[subject].append(grade)
        print(f"✅ Added grade {grade:.1f} for {subject}")
    
    def get_average(self, subject: Optional[str] = None) -> float:
        """
        Calculate average grade.
        
        Args:
            subject (str, optional): Specific subject (None for overall average)
            
        Returns:
            float: The average grade
        """
        if subject:
            # Average for specific subject
            if subject in self.grades and self.grades[subject]:
                return sum(self.grades[subject]) / len(self.grades[subject])
            return 0.0
        else:
            # Overall average across all subjects
            all_grades = []
            for subject_grades in self.grades.values():
                all_grades.extend(subject_grades)
            
            if all_grades:
                return sum(all_grades) / len(all_grades)
            return 0.0
    
    def get_letter_grade(self, average: float) -> str:
        """
        Convert numeric grade to letter grade.
        
        Args:
            average (float): Numeric grade
            
        Returns:
            str: Letter grade (A, B, C, D, F)
        """
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def get_report_card(self) -> None:
        """Print a detailed report card for the student."""
        print(f"\n{'='*60}")
        print(f"REPORT CARD".center(60))
        print(f"{'='*60}")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"{'='*60}")
        
        if not self.grades:
            print("No grades recorded yet.")
        else:
            print(f"\n{'Subject':<20} {'Grades':<25} {'Average':>10} {'Letter':>5}")
            print("-" * 60)
            
            for subject in sorted(self.grades.keys()):
                grades_str = ", ".join(f"{g:.1f}" for g in self.grades[subject])
                avg = self.get_average(subject)
                letter = self.get_letter_grade(avg)
                
                print(f"{subject:<20} {grades_str:<25} {avg:>10.1f} {letter:>5}")
            
            print("-" * 60)
            overall_avg = self.get_average()
            overall_letter = self.get_letter_grade(overall_avg)
            print(f"{'OVERALL':<20} {'':<25} {overall_avg:>10.1f} {overall_letter:>5}")
        
        print("=" * 60)
    
    def get_subjects(self) -> List[str]:
        """
        Get list of all subjects.
        
        Returns:
            List[str]: List of subject names
        """
        return sorted(self.grades.keys())
    
    def remove_grade(self, subject: str, index: int) -> bool:
        """
        Remove a specific grade from a subject.
        
        Args:
            subject (str): The subject name
            index (int): Index of the grade to remove
            
        Returns:
            bool: True if successful, False otherwise
        """
        if subject in self.grades and 0 <= index < len(self.grades[subject]):
            removed = self.grades[subject].pop(index)
            print(f"✅ Removed grade {removed:.1f} from {subject}")
            
            # Remove subject if no grades left
            if not self.grades[subject]:
                del self.grades[subject]
            
            return True
        
        print(f"❌ Invalid subject or grade index")
        return False
    
    def __str__(self) -> str:
        """String representation of the student."""
        avg = self.get_average()
        return f"Student({self.student_id}, {self.name}, Avg: {avg:.1f})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Student(name='{self.name}', age={self.age}, id='{self.student_id}')"


class Classroom:
    """
    Manages a collection of students.
    
    Attributes:
        name (str): Classroom name
        students (List[Student]): List of students in the classroom
    """
    
    def __init__(self, name: str):
        """
        Initialize a new classroom.
        
        Args:
            name (str): Classroom name
        """
        self.name = name
        self.students: List[Student] = []
    
    def add_student(self, student: Student) -> None:
        """
        Add a student to the classroom.
        
        Args:
            student (Student): The student to add
        """
        self.students.append(student)
        print(f"✅ Added {student.name} to {self.name}")
    
    def remove_student(self, student_id: str) -> bool:
        """
        Remove a student by ID.
        
        Args:
            student_id (str): The student's ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                removed = self.students.pop(i)
                print(f"✅ Removed {removed.name} from {self.name}")
                return True
        
        print(f"❌ Student {student_id} not found")
        return False
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Find a student by ID.
        
        Args:
            student_id (str): The student's ID
            
        Returns:
            Optional[Student]: The student if found, None otherwise
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_class_average(self) -> float:
        """
        Calculate the class average.
        
        Returns:
            float: The class average
        """
        if not self.students:
            return 0.0
        
        total = sum(student.get_average() for student in self.students)
        return total / len(self.students)
    
    def get_top_students(self, n: int = 3) -> List[Student]:
        """
        Get the top N students by average grade.
        
        Args:
            n (int): Number of students to return
            
        Returns:
            List[Student]: Top students sorted by grade
        """
        sorted_students = sorted(
            self.students,
            key=lambda s: s.get_average(),
            reverse=True
        )
        return sorted_students[:n]
    
    def list_students(self) -> None:
        """Print all students in the classroom."""
        print(f"\n{'='*60}")
        print(f"{self.name} - Student List".center(60))
        print(f"{'='*60}")
        
        if not self.students:
            print("No students enrolled.")
        else:
            print(f"{'ID':<10} {'Name':<25} {'Age':>5} {'Avg':>10} {'Grade':>5}")
            print("-" * 60)
            
            for student in self.students:
                avg = student.get_average()
                letter = student.get_letter_grade(avg)
                print(f"{student.student_id:<10} {student.name:<25} {student.age:>5} {avg:>10.1f} {letter:>5}")
        
        print("=" * 60)
    
    def __len__(self) -> int:
        """Return the number of students in the classroom."""
        return len(self.students)
    
    def __str__(self) -> str:
        """String representation of the classroom."""
        avg = self.get_class_average()
        return f"Classroom({self.name}, {len(self.students)} students, Avg: {avg:.1f})"


def demo():
    """Demonstrate the Student and Classroom classes."""
    print("🎓 Student Management System Demo\n")
    
    # Create classroom
    classroom = Classroom("Computer Science 101")
    
    # Create students
    alice = Student("Alice Johnson", 20)
    bob = Student("Bob Smith", 21)
    charlie = Student("Charlie Brown", 19)
    
    # Add grades
    print("Adding grades for Alice...")
    alice.add_grade("Mathematics", 95)
    alice.add_grade("Mathematics", 92)
    alice.add_grade("Programming", 88)
    alice.add_grade("Programming", 90)
    alice.add_grade("English", 85)
    
    print("\nAdding grades for Bob...")
    bob.add_grade("Mathematics", 78)
    bob.add_grade("Mathematics", 82)
    bob.add_grade("Programming", 95)
    bob.add_grade("Programming", 98)
    bob.add_grade("English", 80)
    
    print("\nAdding grades for Charlie...")
    charlie.add_grade("Mathematics", 88)
    charlie.add_grade("Programming", 85)
    charlie.add_grade("English", 92)
    
    # Add students to classroom
    print()
    classroom.add_student(alice)
    classroom.add_student(bob)
    classroom.add_student(charlie)
    
    # Show report cards
    alice.get_report_card()
    bob.get_report_card()
    charlie.get_report_card()
    
    # Show classroom info
    classroom.list_students()
    
    print(f"\n📊 Class Average: {classroom.get_class_average():.1f}")
    
    print("\n🏆 Top Students:")
    for i, student in enumerate(classroom.get_top_students(), 1):
        print(f"  {i}. {student.name} - {student.get_average():.1f}")


if __name__ == "__main__":
    demo()