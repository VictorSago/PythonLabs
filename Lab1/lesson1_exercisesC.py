
# Part C - Strings

# Ex 1
sentence = "Don't Panic! "

print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
print()

# Ex 2
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()

print(f"{first_name.title()} {last_name.title()}")
print()

# Ex 3
string = "python programming"
print(string[0])
print(string[-1])
print(string[:6])
print(string[-11:])
print(string[::-1])
print()

# Ex 4
user_name = f"{first_name.lower()[:3]}{last_name.lower()[:5]}"
print(user_name)

print()

# Ex 5
email = input("Email: ").strip()
email_parts = email.split("@")
print("email name:", email_parts[0])
print("email domain:", email_parts[1])
print()

# Ex 6
sentence = "This is a sentence containing Java and other words."
print(sentence)
sentence = sentence.replace("Java", "Python")
print(sentence)
