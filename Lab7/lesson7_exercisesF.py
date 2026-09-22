
# ==========================================================
# Part F - Applied challenge: Course manager
# ==========================================================

# 1. Build a small course management program using Student, Teacher and Course classes.
# 2. Student should contain at least name and score.
# 3. Student should have a method that returns "PASS" or "FAIL".
class Student:
    # This is shared by all students, so it belongs to the class.
    PASSING_SCORE = 75

    def __init__(self, name, score):
        self.name = name
        self.update_score(score)

    def get_status(self):
        if self.score >= Student.PASSING_SCORE:
            return "PASS"
        return "FAIL"

    def update_score(self, new_score):
        self.score = new_score


# 4. Teacher should contain at least a name.
class Teacher:
    def __init__(self, name):
        self.name = name


# 5. Course should contain a name, a Teacher object and a list of Student objects.
# 6. Add methods for adding a student and showing how many students are currently in the course.
# 7. Add a method that returns a list containing only the students who passed.
# 8. Add validation somewhere in your program using ValueError.
class Course:
    def __init__(self, name, teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError("teacher must be a Teacher object")
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Only Student objects can be added")
        self.students.append(student)

    def student_count(self):
        return len(self.students)

    def passed_students(self):
        return [
            student
            for student in self.students
            if student.get_status() == "PASS"
        ]

    def print_summary(self):
        print("Course summary")
        print("Course:", self.name)
        print("Teacher:", self.teacher.name)
        print("Number of students:", self.student_count())
        passed = self.passed_students()
        print("Students who passed:")
        for student in passed:
            print(f" - {student.name}: {student.score}")


# 9. Create at least five Student objects, one Teacher object and one Course object. 
students = [
    Student("Alice", 85),
    Student("Bob", 62),
    Student("Chloe", 91),
    Student("Daniel", 74),
    Student("Eva", 55),
    Student("Frank", 68)
]
teacher1 = Teacher("Prof. Timothy Snyder")
course1 = Course("History of Eastern Europe", teacher1)

for student in students:
    course1.add_student(student)

student2 = students[4]
print(f"Student {student2.name} has score {student2.score}.")
print(f"Student's status is {student2.get_status()}")

student2.update_score(75)
print("After update:")
print(f"Student {student2.name} has score {student2.score}.")
print(f"Student's status is {student2.get_status()}")

print()
print(f"At present, {course1.student_count()} students are attending course '{course1.name}'.")
print("The students with a passing score in this course:")
for student in course1.passed_students():
    print(f" - {student.name}: {student.score}")

# 10. Print a simple course summary containing the course name, teacher name,
# number of students and the names of the students who passed.
print()
print("--- Course Summary ---")
course1.print_summary()
