
# ==========================================================
# PART G - Stretch challenges
# ==========================================================

# 1. merge_settings(defaults, **overrides)
def merge_settings(defaults, **overrides):
    """returns a new dictionary without modifying defaults."""
    # .copy() first, so we're never mutating the caller's original
    # defaults dictionary - update() then happens on the new copy only.
    merged = defaults.copy()
    merged.update(overrides)
    return merged


base_settings = {"theme": "light", "font_size": 12, "language": "en"}
custom_settings = merge_settings(base_settings, theme="dark", font_size=14)

print("Original defaults:", base_settings)     # unchanged
print("Merged settings:", custom_settings)      # new dict, overrides applied


# 2. call_summary(function_name, *args, **kwargs)
# the `!r` inside the f-string tells Python to format the value using
# `repr()` instead of `str()`, which makes that string look like strings.
def call_summary(function_name, *args, **kwargs):
    """a string describing what would be called and with which arguments"""
    arg_parts = [repr(arg) for arg in args]
    kwarg_parts = [f"{key}={value!r}" for key, value in kwargs.items()]
    all_parts = arg_parts + kwarg_parts
    return f"{function_name}({', '.join(all_parts)})"


print(call_summary("add_all", 1, 2, 3))
print(call_summary("greet_with_details", name="Bob", age=25, city="Oslo"))
print(call_summary("calculate_order", "Ada", 20, 35, discount=10))


# 3. A flexible statistics function.
def calculate_statistics(*numbers):
    """returns count, total, average, min, max"""
    count = len(numbers)

    if count == 0:
        return {"count": 0, "total": 0, "average": None, "min": None, "max": None}

    total = 0
    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        total += number
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return {
        "count": count,
        "total": total,
        "average": total / count,
        "min": smallest,
        "max": largest,
    }


print(calculate_statistics(4, 8, 15, 16, 23, 42))
print(calculate_statistics())  # no numbers supplied


# 4. Five "predict the output" scope questions
# prediction first, then verification.

# Prediction 1: This will print 10, then 5 (the local 'x' inside modify_x
# shadows the global 'x' which is never touched).
print("--- Prediction ---")
x = 5

def modify_x():
    x = 10
    print("Inside modify_x:", x)


modify_x()
print("Global x:", x)

# Prediction 2: This will print [1, 2, 3] - lists are mutable, so append()
# inside the function modifies the same list object the caller passed in, 
# even without 'global' (no reassignment happens, just a mutation).
def add_item(target_list):
    target_list.append(3)


numbers_list = [1, 2]
add_item(numbers_list)
print("After add_item:", numbers_list)


# Prediction 3: Prints "outer value" - inner_reader() has no local 'text', so
# it looks outward to the enclosing scope of reader() and finds it there.
def reader():
    text = "outer value"

    def inner_reader():
        print("Inner sees:", text)

    inner_reader()


reader()

# Prediction 4: Leads to an exception - assigning to 'count' anywhere in
# increment()'s body makes Python treat 'count' as local for the **whole**
# function, so the read on the right-hand side of "count = count + 1" fails
# before any assignment has happened, even though a global 'count' does exist.
count = 0

def increment():
    count = count + 1
    print(count)


#increment()    # left commented out so the rest of the script can still run.

# Prediction 5: 100, then 1 - default argument values are evaluated
# __once__, at function definition time, not on every call. Reassigning
# the global 'default_value' afterward has no effect on a default
# that was already bound when the function was defined.
default_value = 100

def show_default(value=default_value):
    print(value)


default_value = 1
print(default_value)    # prints 1, since we've modified the `default_value`
show_default()          # prints 100, not 1
