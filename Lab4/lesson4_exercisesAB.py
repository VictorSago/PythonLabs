
# ==========================================================
# PART A - Function fundamentals
# ==========================================================

# 1. greet(), show_course_name(), print_separator() - called more than once
def greet():
    print("Hello!")


def show_course_name():
    print("Course: Python Fundamentals")


def print_separator():
    print("-" * 30)


greet()
show_course_name()
print_separator()
greet()
print_separator()
show_course_name()

# 2. greet_person(name) and introduce(name, city)
def greet_person(name):
    print(f"Hello, {name}!")


def introduce(name, city):
    print(f"This is {name}, from {city}.")


introduce("Arthur", "London")
greet_person("Arthur")

# 3. add, subtract, multiply, divide - each returns a value
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(add(4, 3))
print(subtract(10, 6))
print(multiply(5, 6))
print(divide(9, 2))

# 4. Demonstrate parameter vs argument in comments, using one function.
# In `def add(a, b):`, the names `a` and `b` are PARAMETERS - they are 
# placeholders defined as part of the function itself, and exist only 
# inside add()'s own scope.
# In the call `add(4, 3)`, the values `4` and `3` are ARGUMENTS - the actual
# data being passed in for this particular call. The same parameters (a, b)
# can receive different arguments on each call.
result_one = add(4, 3)    # arguments: 4 and 3
result_two = add(10, 20)  # arguments: 10 and 20 - same parameters, new values
print(result_one, result_two)


# 5. calculate_area(width, height) - returned value used in another calculation
def calculate_area(width, height):
    return width * height


room_area = calculate_area(4, 5)

# Use the returned value in a further calculation: cost to carpet the room
cost_per_square_meter = 25
total_cost = room_area * cost_per_square_meter

print("Room area:", room_area)
print("Total carpet cost:", total_cost)

# ==========================================================
# PART B - Return values
# ==========================================================

# 1. is_even(number) returning True/False
def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))

# 2. get_larger(a, b) returning the larger value without max()
def get_larger(a, b):
    if b > a:
        return b
    return a


print(get_larger(9, 15))
print(get_larger(20, 3))

# 3. classify_score(score) returning PASS or FAIL
def classify_score(score):
    if score >= 70:
        return "PASS"
    return "FAIL"


print(classify_score(75))
print(classify_score(40))

# 4. full_name(first_name, last_name) returning a formatted string
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(full_name("Ada", "Lovelace"))

# 5. calculate_discount(price, percent) returning the discounted price
def calculate_discount(price, percent):
    return price - (price * percent / 100)


print(calculate_discount(200, 25))

# 6. Show with a small example why print(result) inside a function is
# not the same as return result.

def add_and_print(a, b):
    # This function PRINTS the sum but does not RETURN anything. 
    # Its implicit return value is None.
    print(a + b)


def add_and_return(a, b):
    # This function RETURNS the sum, without printing it itself.
    return a + b


printed_result = add_and_print(3, 4)   # prints "7" as a side effect
returned_result = add_and_return(3, 4)  # prints nothing by itself

print("printed_result is:", printed_result)    # None - nothing was returned
print("returned_result is:", returned_result)  # 7 - the actual value
