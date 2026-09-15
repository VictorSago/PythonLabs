
# ==========================================================
# PART A - Scope
# ==========================================================

# 1. Global variable course_name + a function with a local variable
# of the same name.
course_name = "Introduction to Python"


def show_local_course_name():
    course_name = "Advanced Python"  # this is a LOCAL variable
    print("Inside function:", course_name)


show_local_course_name()
print("Outside function:", course_name)

# Explanation: the assignment inside show_local_course_name() creates a new
# local variable that only exists within that function's scope. It does not 
# touch the global course_name. Once the function returns, its local
# "course_name" is gone, and the global one is as it was before the call.


# 2. A function with a local counter - not available outside it.
def run_with_local_counter():
    counter = 0
    counter += 1
    print("Counter inside function:", counter)


run_with_local_counter()

# print(counter)  # NameError: 'counter' is not defined out here -
# it only ever existed inside run_with_local_counter()'s local scope.


# 3. A function that attempts to modify a global numeric variable
# without 'global' - observe the problem, then fix it by returning
# the new value instead.
score = 10


def increment_score_broken():
    # This does NOT modify the global 'score'. Writing to a name
    # inside a function makes Python treat it as local for the whole
    # function body, so this creates a brand-new local 'score' that
    # shadows the global one - then raises UnboundLocalError, because
    # the right-hand side (score + 1) tries to read 'score' as a
    # local variable before that local has been assigned anything yet.
    score = score + 1
    return score
    # pass


# score = increment_score_broken()
# print("Updated score:", score)

# Fixed design: don't rely on modifying the global in place - just
# return the new value and.
def increment_score(current_score):
    return current_score + 1


score = increment_score(score)
print("Updated score:", score)


# 4. A nested function demonstrating a simple enclosing-scope lookup.
def outer_function():
    message = "Hello from the enclosing scope"

    def inner_function():
        # inner_function doesn't define 'message' itself, so Python looks in 
        # the enclosing scope (outer_function) to find it.
        print(message)

    inner_function()


outer_function()

# 5. Examples that avoid shadowing built-ins such as list, str, sum, max.
numbers = [4, 8, 15, 16, 23, 42]        # not "list"
name_text = "Ada Lovelace"              # not "str"
numbers_total = 0                       # not "sum"
largest_number = numbers[0]             # not "max"

for value in numbers:
    numbers_total += value
    if value > largest_number:
        largest_number = value

print(numbers, name_text, numbers_total, largest_number)


# ==========================================================
# PART B - *args
# ==========================================================

# 1. add_all(*numbers) - sum without sum()
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))


# 2. average(*numbers) - decide what happens with no arguments.
def average(*numbers):
    # With no numbers supplied, there's no average to return. Therefore, 
    # returning `None` is better than raising a ZeroDivisionError or silently
    # returning 0, which could be mistaken for a real average.
    if len(numbers) == 0:
        return None
    return add_all(*numbers) / len(numbers)


print(average(4, 8, 12))
print(average())


# 3. longest_word(*words) - returning the longest word.
def longest_word(*words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("cat", "elephant", "eagle", "hippopotamus"))


# 4. build_sentence(separator, *words) - one joined string.
def build_sentence(separator, *words):
    return separator.join(words)


print(build_sentence(" ", "This", "is", "a", "sentence"))
print(build_sentence(", ", "apples", "bananas", "cherries"))


# 5. describe_scores(student_name, *scores) - name, number of scores,
# and average.
def describe_scores(student_name, *scores):
    score_count = len(scores)
    # not using previously defined `average` because `None` can't be formatted
    score_average = (add_all(*scores) / score_count) if score_count > 0 else 0
    return f"{student_name}: {score_count} scores, average {score_average:.2f}"


print(describe_scores("Alice", 80, 90, 70))
print(describe_scores("Bob", 60, 75))
print(describe_scores("Charlie"))


# ==========================================================
# PART C - Positional unpacking
# ==========================================================

# 1. Unpack [10, 20, 30] into a function expecting three positional
# parameters.
def show_three_values(first, second, third):
    print(first, second, third)


values_list = [10, 20, 30]
show_three_values(*values_list)


# 2. Call a function using *tuple containing first_name, last_name, city
def introduce_person(first_name, last_name, city):
    print(f"{first_name} {last_name} lives in {city}.")


person_tuple = ("Ada", "Lovelace", "London")
introduce_person(*person_tuple)


# 3. Starred assignment: first, *middle, last = values. Test with
# several list lengths.
values_a = [1, 2, 3, 4, 5]
first, *middle, last = values_a
print(first, middle, last)  # 1 [2, 3, 4] 5

values_b = [1, 2]
first, *middle, last = values_b
print(first, middle, last)  # 1 [] 2 - middle is empty with only 2 items

values_c = [1, 2, 3]
first, *middle, last = values_c
print(first, middle, last)  # 1 [2] 3


# 4. Difference between * in a function definition and in a function call.
# In a function definition the star means "PACK any number of positional
# arguments the caller supplies into a single tuple.
# In a function call the star means the opposite: "UNPACK this existing 
# collection into separate individual positional arguments" before the call.
# Short: in a def it GATHERS arguments together; in a call it SPREADS them apart.


# ==========================================================
# PART D - **kwargs
# ==========================================================

# 1. show_profile(**info) - iterate over all key/value pairs.
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_profile(name="Alice", age=30, city="Stockholm")


# 2. create_user(username, **details) - one dictionary containing
# username plus all supplied details.
def create_user(username, **details):
    user = {"username": username}
    user.update(details)
    return user


print(create_user("alice01", email="alice@example.com", age=30))


# 3. build_product(name, price, **metadata) - returning a dictionary.
def build_product(name, price, **metadata):
    product = {"name": name, "price": price}
    product.update(metadata)
    return product


print(build_product("Laptop", 999, brand="TechCo", warranty_years=2))


# 4. A function that accepts **settings and returns only settings
# whose value is not None.
def filter_active_settings(**settings):
    active_settings = {}
    for key, value in settings.items():
        if value is not None:
            active_settings[key] = value
    return active_settings


print(filter_active_settings(theme="dark", font_size=None, language="en"))


# 5. Call a normal named-parameter function using **dictionary
# unpacking. Dictionary keys must match parameter names.
def greet_with_details(name, age, city):
    print(f"Hello {name}, age {age}, from {city}!")


person_details = {"name": "Bob", "age": 25, "city": "Oslo"}
greet_with_details(**person_details)


# ==========================================================
# PART E - Combining parameters
# ==========================================================

# 1. log_event(event_type, *messages, **metadata)
# return a structured dictionary.
def log_event(event_type, *messages, **metadata):
    return {
        "event_type": event_type,
        "messages": list(messages),
        "metadata": metadata,
    }


print(log_event("error", "Disk full", "Retry failed", severity="high", code=500))


# 2. calculate_order(customer, *prices, **options) 
# optional discount and shipping fee in options.
def calculate_order(customer, *prices, **options):
    subtotal = add_all(*prices)
    discount = options.get("discount", 0)
    shipping_fee = options.get("shipping_fee", 0)

    total = subtotal - (subtotal * discount / 100) + shipping_fee

    return {
        "customer": customer,
        "subtotal": subtotal,
        "discount": discount,
        "shipping_fee": shipping_fee,
        "total": total,
    }


print(calculate_order("Carla", 20, 35, 15, discount=10, shipping_fee=5))
print(calculate_order("David", 50, 30))  # no discount/shipping supplied


# 3. A function where explicit named parameters would be clearer than **kwargs
# Version with **kwargs - flexible, but the caller has no idea what keys are
# expected without reading the function body, and a typo in a key name fails 
# silently rather than raising an error.
def calculate_rectangle_area_kwargs(**dimensions):
    return dimensions["width"] * dimensions["height"]


# Version with explicit named parameters - the signature itself documents 
# exactly what's required.
def calculate_rectangle_area_explicit(width, height):
    return width * height


print(calculate_rectangle_area_kwargs(width=4, height=5))
print(calculate_rectangle_area_explicit(4, 5))

# Comparison: **kwargs is genuinely useful when the set of fields is unknown
# or caller-defined, but for a fixed, small, always-required set of values 
# like a rectangle's width and height, explicit parameters are clearer, safer,
# and let tools/IDE autocompletion and error-checking actually help the coder.


# 4. At least three calls to the same flexible function with
# substantially different numbers of arguments.
print(log_event("login"))
print(log_event("purchase", "Item added to cart", item_id=42))
print(log_event("crash", "Null pointer", "Stack overflow", "Timeout", severity="critical", code=500, retry=False))
