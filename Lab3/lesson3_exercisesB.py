
# ==========================================================
# Part B - Truthy, falsy and membership
# ==========================================================s

# 1. Examples with empty/non-empty string, zero/non-zero integer,
# empty/non-empty list - tested directly in an if statement.

empty_string = ""
non_empty_string = "hello"
zero_value = 0
non_zero_value = 42
empty_list = []
non_empty_list = [1, 2, 3]

if empty_string:
    print("empty_string is truthy")
else:
    print("empty_string is falsy")

if non_empty_string:
    print("non_empty_string is truthy")
else:
    print("non_empty_string is falsy")

if zero_value:
    print("zero_value is truthy")
else:
    print("zero_value is falsy")

if non_zero_value:
    print("non_zero_value is truthy")
else:
    print("non_zero_value is falsy")

if empty_list:
    print("empty_list is truthy")
else:
    print("empty_list is falsy")

if non_empty_list:
    print("non_empty_list is truthy")
else:
    print("non_empty_list is falsy")


# 2. Check whether a language exists in a predefined list of supported languages.
print("--2--")
supported_languages = ["python", "javascript", "java", "c++", "rust"]

chosen_language = input("Enter a programming language: ")

if chosen_language.lower() in supported_languages:
    print(chosen_language, "is supported")
else:
    print(chosen_language, "is not supported")


# 3. Check whether a username is in the list of blocked usernames
# and reject it if it appears in the list.
print("--3--")
blocked_usernames = ["admin", "root", "test", "guest"]

supplied_username = input("Choose a username: ")

if supplied_username in blocked_usernames:
    print("Username is blocked. Please choose another.")
else:
    print("Username accepted.")


# 4. Use `not` to express at least two conditions in a readable way.
print("--4--")
is_logged_in = True
has_permission = False

# Readable with 'not': block access when the user is not logged in.
if not is_logged_in:
    print("Please log in first.")

# Readable with 'not': warn when permission has not been granted,
# even if the user is logged in.
if is_logged_in and not has_permission:
    print("You are logged in but do not have permission.")
