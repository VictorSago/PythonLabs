
# ==========================================================
# Part A - Conditions
# ==========================================================

# 1. Classify a number as positive, negative or zero
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. Ask for an age and classify it into at least four age groups
print("--2--")
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 3. Login check using a stored username and password - both must match
print("--3--")
stored_username = "admin"
stored_password = "secret123"
entered_username = input("Username: ")
entered_password = input("Password: ")
if entered_username == stored_username and entered_password == stored_password:
    print("Login successful")
else:
    print("Login failed")

# 4. Given a score from 0-100, print a grade using at least five ranges
# Condition order matters: check from highest to lowest, since the
# first matching branch wins and elif stops further checks.
print("--4--")
score = float(input("Enter score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

# 5. Shipping rule based on order total and membership status
print("--5--")
order_total = float(input("Order total: "))
# `is_member` will be a boolean. 
# The parenthesis aren't necessary, but they increase readability
is_member = (input("Are you a member? (yes/no): ").strip().lower() == "yes")
# Free shipping if the order is large enough, OR if the customer is a
# member and still spent a reasonable amount.
if order_total >= 100 or (is_member and order_total >= 50):
    print("Free shipping")
else:
    print("Standard shipping fee applies")

# 6. Five expressions using comparison operators - predict, then check
print("--6--")
a = 7
b = 3
# Prediction: False  (7 is not equal to 3)
print(a == b)
# Prediction: True  (7 is indeed not equal to 3)
print(a != b)
# Prediction: True  (7 is greater than 3)
print(a > b)
# Prediction: False (7 is not less than 3)
print(a < b)
# Prediction: True  (7 is greater than or equal to 3)
print(a >= b)
