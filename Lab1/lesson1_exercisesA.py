
# Part A - Warm-up

# Ex 1
name = "Victor"
course_name = "Python and AI Development (2026)"
study_goal = "Python Fundamentals"

print("Name: ", name)
print("Course: ", course_name)
print("Today's study goal: ", study_goal)
print()

# Ex 2
person_name = "Zaphod Beeblebrox"
person_age = 242
person_height = 2.16
person_is_student = False
print(f"Name (Type: {type(person_name)}): {person_name}")
print(f"Age (Type: {type(person_age)}): {person_age}")
print(f"Height (Type: {type(person_height)}): {person_height}")
print(f"Is a student (Type: {type(person_is_student)}): {person_is_student}")
print()

# Ex 3
print(f"Type of variable 'person_age' before is: {type(person_age)}")
person_age *= 1.1
print(f"Type of variable 'person_age' after is: {type(person_age)}")
# Python has dynamic typing, which means that variable name aren't bound to one
# specific type, but can hold values of any type.
print()

# Ex 4
a = 10
b = 3
print("Adding a and b: ", a + b)
print("Subtracting a and b: ", a - b)
print("Multiplying a and b: ", a * b)
print("Dividing a and b: ", a / b)
print("Floor division of a and b: ", a // b)
print("Modulo operation a by b: ", a % b)
print("Raising a to power b: ", a ** b)
