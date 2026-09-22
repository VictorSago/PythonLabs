
# ==========================================================
# Part G - Stretch challenges
# ==========================================================

# 1. Flatten a simple list of lists using a comprehension.
nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# This works only of every element in the list is also a list or an iterable.
# For a mixed list there is a little more code
flattened = [item for sublist in nested_lists for item in sublist]
print(flattened)

mixed_list = [1, [2, 3], 4, [5, 6, 7], 8, [9, 10]]
# This works mixed lists too
flattened_mixed = [
    item
    for element in mixed_list
    for item in (element if isinstance(element, list) else [element])
]
print(flattened_mixed)


# 2. A multiplication table structure using a nested comprehension -
# then decide whether the result is readable enough.
multiplication_table = [[row * column for column in range(1, 11)] for row in range(1, 11)]
print(multiplication_table)

for row in multiplication_table:
    print(row)

# Readability: the comprehension that builds the table is reasonably readable
# on its own - "for each row, for each column, multiply them" reads fairly
# naturally as one line. But the result itself (a list of lists of numbers) is
# much easier for a human to actually read when printed row by row afterward,
# rather than as one flat printed list of lists.


# 3. Given names and scores, create only passing student dictionaries
# in one readable comprehension.
student_names = ["Alice", "Bob", "Carla", "David"]
student_scores = [85, 55, 91, 40]
passing_score = 70

passing_students = [
    {"name": name, "score": score}
    for name, score in zip(student_names, student_scores)
    if score >= passing_score
]
print(passing_students)


# 4. Use any() and all() to answer useful questions about a score
# list, after first solving them with loops.
test_scores = [72, 88, 91, 65, 78]
passing_threshold = 60

# with loops first
any_failing_loop = False
for score in test_scores:
    if score < passing_threshold:
        any_failing_loop = True
        break

all_passing_loop = True
for score in test_scores:
    if score < passing_threshold:
        all_passing_loop = False
        break

print("Any failing (loop):", any_failing_loop)
print("All passing (loop):", all_passing_loop)

# with any()/all()
any_failing = any(score < passing_threshold for score in test_scores)
all_passing = all(score >= passing_threshold for score in test_scores)

print("Any failing (any/all):", any_failing)
print("All passing (any/all):", all_passing)


# 5. Five examples where Pythonic syntax reduces boilerplate without
# reducing clarity.

# (1) List comprehension instead of a manual filter loop.
even_numbers = [number for number in range(1, 21) if number % 2 == 0]

# (2) dict(zip(...)) instead of a manual loop building a dictionary
# key by key.
paired_dict = dict(zip(["a", "b", "c"], [1, 2, 3]))

# (3) Tuple-unpacking swap instead of a temporary variable.
x, y = 5, 10
x, y = y, x

# (4) any()/all() instead of a manual flag-and-loop pattern.
has_negative = any(value < 0 for value in [4, -2, 7, 9])

# (5) sorted(..., key=...) with a lambda instead of writing a manual
# comparison-based sort from scratch.
sorted_by_length = sorted(["python", "cat", "elephant"], key=len)

print(even_numbers)
print(paired_dict)
print(x, y)
print(has_negative)
print(sorted_by_length)

# Each of these replaces several lines of manual loop and bookkeeping code
# with one line that still reads as a direct statement of intent. 
# The boilerplate disappears, the intent of the code is clearer.
