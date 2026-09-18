
# ==========================================================
# Part F - Stretch challenges Python Foundation
# ==========================================================

# 1. Create a simple seconds converter: input total seconds and calculate 
# whole hours, minutes, and seconds.
total_seconds = int(input("Total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
print()


# 2. Given a four-digit integer, extract and print each digit without converting the number to a string.
number = 2468
print("Full number:", number)
print(f"First: {number // 1000}, Second: {number % 1000 // 100}")
print(f"Third: {number % 100 // 10}, Fourth: {number % 10}")
print()

# 3. Create a text masking program that displays only the first two and last
# two characters of a supplied word, replacing the middle with * characters.
supplied_word = "SomeLongWord"
print(supplied_word[:2] + "*" * (len(supplied_word) - 4) + supplied_word[-2:])
print()


# 4. Write five short 'predict before running' examples that you could give to
# another student. Include at least one type conversion and two string slices.

# Example 1 - type conversion
# Predict: 50
print(int("42") + 8)

# Example 2 - string slice
# Predict: World
print("Hello World"[6:])

# Example 3 - string slice
# Predict: nohtyP
print("Python"[::-1])

# Example 4 - floor division and modulo
# Predict: 4 1
print(17 // 4, 17 % 4)

# Example 5 - string method chaining
# Predict: DATA SCIENCE
print(" Data Science ".strip().upper())
