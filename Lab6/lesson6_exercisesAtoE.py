
# ==========================================================
# Part A - List comprehensions
# ==========================================================

# 1. Squares for numbers 1-20: normal loop, then a list comprehension.
squares_loop = []
for number in range(1, 21):
    squares_loop.append(number ** 2)

squares_comprehension = [number ** 2 for number in range(1, 21)]

print(squares_loop)
print(squares_comprehension)


# 2. A list containing only even numbers from 1-100.
even_numbers = [number for number in range(1, 101) if number % 2 == 0]
print(even_numbers)


# 3. Convert a list of names to stripped, title-cased names.
raw_names = ["  alice", "BOB ", " charles third ", "DAVID"]
cleaned_names = [name.strip().title() for name in raw_names]
print(cleaned_names)


# 4. Given scores, create a list containing only passing scores.
scores = [55, 72, 90, 68, 40, 85, 30]
pass_threshold = 60
passing_scores = [score for score in scores if score >= pass_threshold]
print(passing_scores)


# 5. Labels such as 'PASS'/'FAIL' for every score using a conditional
# expression in a comprehension.
score_labels = ["PASS" if score >= pass_threshold else "FAIL" for score in scores]
print(score_labels)


# 6. Rewrite three earlier loop-based transformations as comprehensions.

# (a) From LAb 3, Part C, exercise 2: a loop through numbers 1-50 printing 
# only even numbers. We'll make it into list created with list comprehension.
# (a) From Lab 3, Part C exercise 2: loop over numbers 1-50 and keep
# only the even ones - originally printed each match; adapted here to
# collect them into a list so it's directly comparable to the
# comprehension version below.
even_numbers_loop = []
for number in range(1, 51):
    if number % 2 == 0:
        even_numbers_loop.append(number)

even_numbers_comprehension = [number for number in range(1, 51) if number % 2 == 0]

print(even_numbers_loop)
print(even_numbers_comprehension)

# (b) From Lab 4, Part D, exercise 3: get_long_words(words, minimum_length), 
# which built a list with an explicit loop and .append().
words = ["cat", "python", "sun", "elephant", "sky"]
def get_long_words_loop(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) > minimum_length:
            long_words.append(word)
    return long_words

def get_long_words_comprehension(words, minimum_length):
    return [word for word in words if len(word) >= minimum_length]

long_words_loop = get_long_words_loop(words, 4)
long_words_comprehension = get_long_words_comprehension(words, 4)

print(long_words_loop, long_words_comprehension)

# (c) From Lab 4, Part D, exercise 6: get_active_users(users), 
# filtering dictionaries where active is True.
users = [
    {"name": "David", "city": "Unknown", "active": True},
    {"name": "Eva", "city": "Berlin", "active": True},
    {"name": "Frank", "city": "Unknown", "active": False},
    {"name": "Grace Hopper", "city": "New York City", "active": False},
    {"name": "Gustav", "city": "Oslo", "active": True},
    {"name": "Helene", "city": "Paris", "active": False},
    {"name": "Iryna", "city": "Kyiv", "active": True},
]
def get_active_users_loop(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users

active_users_loop = get_active_users_loop(users)
active_users_comprehension = [user for user in users if user["active"]]
print(active_users_loop, active_users_comprehension)


# ==========================================================
# Part B - Dictionary and set comprehensions
# ==========================================================

print("========== Part B ==========")

# 1. A dictionary mapping numbers 1-10 to their squares.
squares_dict = {number: number ** 2 for number in range(1, 11)}
print(squares_dict)


# 2. Given a list of words, a dictionary mapping each word to its length.
word_list = ["python", "code", "dictionary", "set", "comprehension", "data"]
word_lengths = {word: len(word) for word in word_list}
print(word_lengths)


# 3. Given a list with duplicates, a set comprehension containing
# lowercase normalized values.
raw_tags = ["Python", "python", "DATA", "Data", "AI", "ai", "Set"]
normalized_tags = {tag.lower() for tag in raw_tags}
print(normalized_tags)


# 4. A dictionary of only products whose price is below a chosen threshold.
products = {"Laptop": 999, "Mouse": 25, "Keyboard": 45, "Monitor": 250, "Cable": 8}
price_threshold = 100
affordable_products = {name: price for name, price in products.items() if price < price_threshold}
print(affordable_products)


# 5. A dictionary mapping student names to PASS/FAIL from a list 
# of student dictionaries.
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charles", "score": 91},
    {"name": "Diana", "score": 60}
]
passing_score = 70
student_results = {student["name"]: ("PASS" if student["score"] >= passing_score else "FAIL") for student in students}
print(student_results)


# ==========================================================
# Part C - enumerate
# ==========================================================

print("========== Part C ==========")

# 1. Print a playlist with numbering starting at 1 using enumerate.
playlist = ["Bohemian Rhapsody", "Imagine", "Hotel California"]
for track_number, song in enumerate(playlist, start=1):
    print(f"{track_number}. {song}")


# 2. Given a list of tasks, print 'Task 1:', 'Task 2:' etc.
tasks = ["Write report", "Review code", "Deploy app"]
for task_number, task in enumerate(tasks, start=1):
    print(f"Task {task_number}: {task}")


# 3. Find and print indexes of all values above a threshold.
values = [12, 42, 7, 89, 34, 6, 90, 5]
threshold = 40
above_threshold_indexes = [index for index, value in enumerate(values) if value > threshold]
print(above_threshold_indexes)


# 4. Rewrite a range(len(...)) loop using enumerate; explain why it's clearer.
items = ["apple", "banana", "cherry"]

# Original style
for index in range(len(items)):
    print(index, items[index])

# Rewritten with enumerate
for index, item in enumerate(items):
    print(index, item)

# Why the enumerate version is clearer:
# range(len(items)) requires accessing 'item' by indexing into `itmes` inside
# the loop body to get the actual value - the loop variable 'index' alone
# doesn't tell you anything about the item itself. `enumerate(items)` gives
# both the index AND the item directly as a pair, so there's no separate 
# lookup step, no risk of indexing the wrong list by mistake, and the loop 
# reads as "for each index, item pair" rather than "for each number, then go fetch the item."


# ==========================================================
# Part D - zip and unpacking
# ==========================================================
print("========== Part D ==========")

# 1. Combine separate name and score lists using zip and print each pair.
names = ["Alice", "Bob", "Carla"]
scores = [85, 72, 91]

for name, score in zip(names, scores):
    print(name, score)


# 2. A dictionary using dict(zip(keys, values)).
keys = ["name", "age", "city"]
values = ["David", 30, "Berlin"]

person = dict(zip(keys, values))
print(person)


# 3. Combine three lists: product name, price and stock.
product_names = ["Laptop", "Mouse", "Keyboard"]
product_prices = [999, 25, 45]
product_stock = [10, 150, 80]

# for name, price, stock in zip(product_names, product_prices, product_stock):
#     print(f"{name}: {price}€, {stock} in stock")

products = list(zip(product_names, product_prices, product_stock))
print("Zipped products:", products)


# 4. Investigate what happens when zipped lists have different lengths.
short_list = [1, 2, 3]
long_list = ["a", "b", "c", "d", "e"]

zipped_result = list(zip(long_list, short_list))
print(zipped_result)

# zip() stops as soon as the SHORTEST iterable is exhausted - it does
# not raise an error, and it does not pad the shorter one with None
# or anything else.


# 5. Use tuple unpacking directly in a for loop over zipped data.
first_names = ["Ada", "Grace", "Alan"]
last_names = ["Lovelace", "Hopper", "Turing"]

for first_name, last_name in zip(first_names, last_names):
    print(f"{first_name} {last_name}")


# 6. Swap two variables without a temporary variable.
a = 5
b = 10

a, b = b, a

print("a:", a, "b:", b)


# ==========================================================
# Part E - sorted and lambda
# ==========================================================
print("========== Part E ==========")

# 1. Sort a list of words by length using sorted(..., key=...).
words = ["python", "cat", "elephant", "sun", "programming"]
words_by_length = sorted(words, key=len)
print(words_by_length)


# 2. Sort a list of student dictionaries by score, ascending and descending.
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Carla", "score": 91},
]

students_ascending = sorted(students, key=lambda student: student["score"])
students_descending = sorted(students, key=lambda student: student["score"], reverse=True)

print(students_ascending)
print(students_descending)


# 3. Sort products by price using a lambda.
products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 45},
]

products_by_price = sorted(products, key=lambda product: product["price"])
print(products_by_price)


# 4. Sort people by last name when each item is a dictionary containing
# first_name and last_name.
people = [
    {"first_name": "Ada", "last_name": "Lovelace"},
    {"first_name": "Alan", "last_name": "Turing"},
    {"first_name": "Grace", "last_name": "Hopper"},
]

people_by_last_name = sorted(people, key=lambda person: person["last_name"])
print(people_by_last_name)


# 5. A normal named function for a sort key, then replace it with lambda.
# Compare when each is clearer.

def get_score(student):
    return student["score"]


students_named_function = sorted(students, key=get_score)
students_lambda = sorted(students, key=lambda student: student["score"])

print(students_named_function)
print(students_lambda)

# Comparison:
# For a short, one-time, "just get out this one field" key like this, lambda
# is clearer - it's a single, self-contained line, and there's no need to 
# invent and remember a throwaway function name that likely won't be reused
# anywhere else in the program. A named function becomes preferable once the
# key logic gets more complex (multiple lines, or is reused in several
# different sorted()/filter()/map() calls) - at that point a lambda crammed
# with logic hurts readability more than it saves typing.
