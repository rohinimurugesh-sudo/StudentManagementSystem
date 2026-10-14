
import unittest
from student import add_student


class TestStudentManagementSystem(unittest.TestCase):

    def test_valid_student(self):
        student = add_student(101, "Arun", 85)
        self.assertEqual(student.name, "Arun")
        self.assertEqual(student.marks, 85)

    def test_grade_a(self):
        student = add_student(102, "Bala", 95)
        self.assertEqual(student.calculate_grade(), "A")

    def test_grade_b(self):
        student = add_student(103, "Cathy", 80)
        self.assertEqual(student.calculate_grade(), "B")

    def test_grade_c(self):
        student = add_student(104, "David", 60)
        self.assertEqual(student.calculate_grade(), "C")

    def test_grade_f(self):
        student = add_student(105, "Eva", 30)
        self.assertEqual(student.calculate_grade(), "F")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            add_student(106, "Ravi", 120)

    def test_negative_marks(self):
        with self.assertRaises(ValueError):
            add_student(107, "Rani", -5)


if __name__ == "__main__":
    unittest.main()
