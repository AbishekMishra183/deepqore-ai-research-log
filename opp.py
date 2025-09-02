# ===========================
# OOP Comprehensive Example
# ===========================

from abc import ABC, abstractmethod

# ---------------------------
# Base class - Abstract
# ---------------------------
class Person(ABC):
    def __init__(self, name, age):
        self._name = name        # protected attribute
        self.__age = age         # private attribute

    @abstractmethod
    def get_info(self):
        pass

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

    # Encapsulation example
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# ---------------------------
# Inheritance: Single
# ---------------------------
class Student(Person):
    school_name = "XYZ School"  # class attribute

    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades  # dictionary of subjects

    def get_info(self):
        return f"Student: {self.name}, Age: {self.get_age()}, ID: {self.student_id}"

    # Method Overriding (Polymorphism)
    def __str__(self):
        return f"{self.name} ({self.student_id}) - Average Grade: {self.average_grade()}"

    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    # Class Method
    @classmethod
    def get_school(cls):
        return cls.school_name

    # Static Method
    @staticmethod
    def school_motto():
        return "Knowledge is Power"

# ---------------------------
# Multiple Inheritance
# ---------------------------
class Sports:
    def __init__(self, sport_name, level):
        self.sport_name = sport_name
        self.level = level

    def sport_info(self):
        return f"{self.sport_name} - Level: {self.level}"

class Athlete(Student, Sports):
    def __init__(self, name, age, student_id, grades, sport_name, level):
        Student.__init__(self, name, age, student_id, grades)
        Sports.__init__(self, sport_name, level)

    # Method Overriding
    def get_info(self):
        return f"{self.name} ({self.student_id}), Age: {self.get_age()}, Sport: {self.sport_name}"

# ---------------------------
# Multilevel Inheritance
# ---------------------------
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, grades, thesis_title):
        super().__init__(name, age, student_id, grades)
        self.thesis_title = thesis_title

    def get_info(self):
        return f"Graduate Student: {self.name}, Thesis: {self.thesis_title}"

# ---------------------------
# Main Program
# ---------------------------
def main():
    # Student object
    grades = {"Math": 90, "Science": 85, "English": 88}
    student1 = Student("Alice", 20, "S123", grades)
    print(student1.get_info())
    print(student1)
    print("School:", Student.get_school())
    print("Motto:", Student.school_motto())
    print()

    # Graduate student
    grad_student = GraduateStudent("Bob", 25, "G456", {"Math": 92, "Physics": 89}, "AI in Healthcare")
    print(grad_student.get_info())
    print()

    # Athlete with multiple inheritance
    athlete1 = Athlete("Charlie", 22, "S789", {"Math": 75, "English": 80}, "Basketball", "Intermediate")
    print(athlete1.get_info())
    print("Average Grade:", athlete1.average_grade())
    print("Sport Info:", athlete1.sport_info())
    print()

    # Encapsulation demo
    print("Original Age:", student1.get_age())
    student1.set_age(21)
    print("Updated Age:", student1.get_age())

    # Property demo
    print("Original Name:", student1.name)
    student1.name = "Alicia"
    print("Updated Name:", student1.name)

if __name__ == "__main__":
    main()
