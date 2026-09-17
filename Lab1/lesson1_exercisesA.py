
# ==========================================================
# Part A - Warm-up: Python basics
# ==========================================================

# 1. Print your name, the course name and today's study goal on separate lines.
name = "Victor"
course_name = "Python and AI Development (2026)"
study_goal = "Python Fundamentals"

print("Name: ", name)
print("Course: ", course_name)
print("Today's study goal: ", study_goal)
print()

# 2. Create variables for a person's name, age, height in meters and whether
# they are currently a student, and print both the values and their types.
person_name = "Zaphod Beeblebrox"
person_age = 242
person_height = 2.16
person_is_student = False
print(f"Name (Type: {type(person_name)}): {person_name}")
print(f"Age (Type: {type(person_age)}): {person_age}")
print(f"Height (Type: {type(person_height)}): {person_height}")
print(f"Is a student (Type: {type(person_is_student)}): {person_is_student}")
print()

# 3. Change the value stored in one variable to a different data type, and 
# print its type before and after the change. Explain in a comment.
print(f"Type of variable 'person_age' before is: {type(person_age)}")
person_age *= 1.1
print(f"Type of variable 'person_age' after is: {type(person_age)}")
# Python has dynamic typing, which means that variable name aren't bound to 
# one specific type, but can hold values of any type.
print()

# 4. Create two numeric variables and apply all the elementary operations.
# Print a readable label before each result.
a = 10
b = 3
print("Adding a and b:", a + b)
print("Subtracting a and b:", a - b)
print("Multiplying a and b:", a * b)
print("Dividing a and b:", a / b)
print("Floor division of a and b:", a // b)
print("Modulo (remainder) a by b:", a % b)
print("Raising a to power b:", a ** b)
print()

# 5. Write three examples where explicit type conversion is necessary: 
# string to int, int to float and number to string.

# String to int - necessary before doing integer arithmetic.
# In practice the text might come from input(), which always returns a string,
# but here it's just a plain string literal instead, to isolate the conversion.
quantity_text = "5"
quantity_number = int(quantity_text)
incremented_quantity = quantity_number + 2
# quantity_text + 2 would raise TypeError - the conversion above isn't 
# optional, since "+" refuses to mix a string and a number.
print("Quantity as text:", quantity_text, ", incremented quantity:", incremented_quantity)

# Int to float - necessary to get a float result out of floor division, for example.
# Normal division already returns a float, so no conversion is needed there, 
# but floor division returns an int when both operands are ints, even if a 
# float result is what's needed further down the program.
total_items = 7
number_of_boxes = 2
whole_boxes = total_items // number_of_boxes
whole_boxes_as_float = float(total_items) // number_of_boxes
print("Whole boxes (int):", whole_boxes, ", whole boxes (float):", whole_boxes_as_float)

# Number to string - necessary before concatenating with + into one string.
# "Age: " + person_age would raise TypeError. Python won't implicitly convert
# a number to text the way an f-string would, so str() is required here.
person_age = 42
age_message = "Age: " + str(person_age)
print(age_message)
