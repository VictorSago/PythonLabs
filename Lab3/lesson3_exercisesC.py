
# ==========================================================
# Part C - For loops
# ==========================================================

# 1. Loop over a list of names and print a numbered greeting for each.
names = ["Alice", "Bob", "Carla", "David"]

for index, name in enumerate(names, start=1):
    print(f"{index}. Hello, {name}!")

# 2. Loop over numbers 1-50 and print only even numbers.
for number in range(1, 51):
    if number % 2 == 0:
        print(number, end=" ")
print()

# 3. Calculate the sum of a list manually using a loop rather than sum().
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for value in numbers:
    total += value

print("Manual sum:", total)

# 4. Find the largest number in a list manually without max().
numbers = [4, 8, 15, 16, 23, 42, 35, -100]

largest = numbers[0]
for value in numbers:
    if value > largest:
        largest = value

print("Largest number:", largest)

# 5. Count how many words in a list have more than five characters.
words = ["python", "cat", "programming", "loop", "elephant", "sun"]

long_word_count = 0
for word in words:
    if len(word) > 5:
        long_word_count += 1

print("Words longer than 5 characters:", long_word_count)

# 6. Given a list of scores, count passes and failures using a threshold of 70.
scores = [55, 72, 90, 68, 70, 45, 88, 32]

passes = 0
failures = 0
for score in scores:
    if score >= 70:
        passes += 1
    else:
        failures += 1

print("Passes:", passes)
print("Failures:", failures)

# 7. Loop over a dictionary using keys, values and .items() in three separate examples.
student_grades = {"Alice": "A", "Bob": "B", "Carla": "C"}

# Using keys
print("--- Keys ---")
for student in student_grades:
    print(student)

# Using .values()
print("--- Values ---")
for grade in student_grades.values():
    print(grade)

# Using .items()
print("--- Items ---")
for student, grade in student_grades.items():
    print(student, "--", grade)
