
# ==========================================================
# Parts F & G - Applied challenge: Course manager & Stretch challenges
# ==========================================================

# F1. Build a small course management program using Student, Teacher and Course classes.
# F2. Student should contain at least name and score.
# F3. Student should have a method that returns "PASS" or "FAIL".
# G1. Add a method that updates a student's score with validation.
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
        if not isinstance(new_score, (int, float)) or not 0 <= new_score <= 100:
            raise ValueError("Score must be a number between 0 and 100.")
        self.score = new_score


# F4. Teacher should contain at least a name.
class Teacher:
    def __init__(self, name):
        self.name = name


# F5. Course should contain a name, a Teacher object and a list of Student objects.
# F6. Add methods for adding a student and showing how many students are currently in the course.
# F7. Add a method that returns a list containing only the students who passed.
# F8. Add validation somewhere in your program using ValueError.
# G2. Add a method to Course that finds students above a score threshold.
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
        
    def students_above_score(self, threshold):
        return [
            student
            for student in self.students
            if student.score > threshold
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


# F9. Create at least five Student objects, one Teacher object and one Course object. 
students = [
    Student("Alice", 85),
    Student("Bob", 62),
    Student("Chloe", 91),
    Student("Daniel", 74),
    Student("Eva", 55),
    Student("Frank", 68)
]
teacher_1 = Teacher("Prof. Timothy Snyder")
course_1 = Course("History of Eastern Europe", teacher_1)

for student in students:
    course_1.add_student(student)

student_2 = students[4]
print(f"Student {student_2.name} has score {student_2.score}.")
print(f"Student's status is {student_2.get_status()}")

student_2.update_score(75)
print("After update:")
print(f"Student {student_2.name} has score {student_2.score}.")
print(f"Student's status is {student_2.get_status()}")

print()
print(f"At present, {course_1.student_count()} students are attending course '{course_1.name}'.")
print("The students with a passing score in this course:")
for student in course_1.passed_students():
    print(f" : {student.name} - {student.score} - {student.get_status()}")

# F10. Print a simple course summary containing the course name, teacher name,
# number of students and the names of the students who passed.
print()
print("--- Course Summary ---")
course_1.print_summary()


# G3. Create another Course object and show that its student list is separate from the first course.
another_teacher = Teacher("Prof. Sarah Paine")
another_course = Course("History of Naval Strategy", another_teacher)

another_student1 = Student("Grace", 88)
another_student2 = Student("Henry", 98)
another_student3 = Student("Iris", 67)
another_course.add_student(another_student1)
another_course.add_student(another_student2)
another_course.add_student(another_student3)


print("\nFirst course students:", course_1.student_count())
for student in course_1.students:
    print(f" : {student.name} - {student.score} - {student.get_status()}")
print("\nSecond course students:", another_course.student_count())
for student in another_course.students:
    print(f" : {student.name} - {student.score} - {student.get_status()}")

print(course_1.students is another_course.students)
# False

# G4. Add one useful class attribute to Student, Teacher or Course and explain
# in a comment why it belongs to the class rather than an individual object.
#   The class attribute chosen for this exercise is Student.PASSING_SCORE. It
#   belongs to the class rather than to an individual Student object because
#   it represents a rule of the grading system itself, not a property of any
#   one student - every Student should be judged against the exact same passing
#   threshold. Storing it once, on the class, guarantees that; storing it as an
#   instance attribute instead would let two different Student objects end up
#   with different thresholds by accident, with nothing in the code preventing
#   that from happening.
