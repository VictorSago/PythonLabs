
# ==========================================================
# Part C - Strings
# ==========================================================

# 1. Store a full sentence in a variable, then print its length, uppercase
# version, lowercase version, and a version with surrounding whitespace removed.
sentence = "Don't Panic! "
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
print()

# 2. Ask for first and last names. Create a formatted full name with an f-string.
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
print(f"{first_name.title()} {last_name.title()}")
print()

# 3. Given the string 'python programming', print the first character, last
# character, first 6 characters, last eleven characters and the entire string reversed.
string = "python programming"
print(string[0])
print(string[-1])
print(string[:6])
print(string[-11:])
print(string[::-1])
print()

# 4. Username generator: ask for first and last name, remove surrounding spaces,
# convert to lowercase and create a username using the first 3 letters of the
# first name + the first 5 letters of the last name.
# Reusing the `first_name` and `last_name` from exercise 2.
user_name = f"{first_name.lower()[:3]}{last_name.lower()[:5]}"
print("User Name:", user_name)
print()

# 5. Given an email address, extract the part before @ and the domain after @.
# Assume exactly one @ for this exercise.
email = input("Email: ").strip()
email_parts = email.split("@")
print("email name:", email_parts[0])
print("email domain:", email_parts[1])
print()

# 6. Create a sentence containing the word 'Java', then replace it with 
# 'Python', and print both the original and changed sentence.
java_sentence = "This is a sentence containing Java and other words."
print(java_sentence)
java_sentence = java_sentence.replace("Java", "Python")
print(java_sentence)
