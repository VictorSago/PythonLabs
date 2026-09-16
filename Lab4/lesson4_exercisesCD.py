
# ==========================================================
# PART C - Defaults and keyword arguments
# ==========================================================

# 1. greet(name, greeting='Hello'). Test positional and keyword arguments.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")                              # uses the default greeting
greet("Bob", "Welcome")                     # positional argument overrides default
greet("Carla", greeting="Good morning")     # keyword argument overrides default

# 2. calculate_price(price, quantity=1, discount=0). 
# `discount` is in percent. Return the final total.
def calculate_price(price, quantity=1, discount=0):
    subtotal = price * quantity
    return subtotal - (subtotal * discount / 100)


print(calculate_price(10))                              # just price, defaults used
print(calculate_price(10, 3))                           # price + quantity
print(calculate_price(10, 3, 20))                       # price + quantity + discount
print(calculate_price(10, quantity=2, discount=10))     # keyword arguments

# 3. create_profile(name, city='Unknown', active=True) returning a dictionary
def create_profile(name, city="Unknown", active=True):
    return {"name": name, "city": city, "active": active}


users = []
users.append(create_profile("David"))
users.append(create_profile("Eva", "Berlin"))
users.append(create_profile("Frank", active=False))

# 4. Call one function using keyword arguments in a different order
profile = create_profile(active=False, name="Grace Hopper", city="New York City")
users.append(profile)

for user in users:
    print(user)

# 5. One invalid default-parameter ordering, as a comment.
#
# def broken_function(name, greeting="Hello", city):
#     print(greeting, name, city)
#
# This is invalid because in a function definition, every parameter
# that has a default value must come AFTER all parameters that don't
# have one. Here, 'city' (no default) appears after 'greeting'
# (which has a default), so it raises:
#   SyntaxError: non-default argument follows default argument

# ==========================================================
# PART D - Functions and collections
# ==========================================================

# 1. calculate_total(numbers) manually using a loop
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(calculate_total([4, 8, 15, 16, 23, 42]))

# 2. count_even(numbers)
def count_even(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count


print(count_even([1, 2, 3, 4, 5, 6, 7, 8]))

# 3. get_long_words(words, minimum_length) and return a new list
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) > minimum_length:
            long_words.append(word)
    return long_words


print(get_long_words(["cat", "python", "sun", "elephant", "sky"], 4))

# 4. find_student(students, name) - students is a list of dictionaries.
# Return the matching dictionary or None.
def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Carla", "score": 91},
]

print(find_student(students, "Bob"))
print(find_student(students, "Zoe"))

# 5. average_score(students) - list of dictionaries containing score values
def average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


print(average_score(students))

# 6. get_active_users(users) - returning only dictionaries where active is True
def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users


users2 = [
    {"name": "Gustav", "city": "Oslo", "active": True},
    {"name": "Helene", "city": "Paris", "active": False},
    {"name": "Iryna", "city": "Kyiv", "active": True},
]
users.extend(users2)

print(get_active_users(users))
