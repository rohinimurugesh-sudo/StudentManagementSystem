
class Student:
    def __init__(self, roll_no, name, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"


def add_student(roll_no, name, marks):
    return Student(roll_no, name, marks)
