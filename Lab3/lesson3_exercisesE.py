
# ==========================================================
# Part E - While loops
# ==========================================================

# 1. Create a countdown from 10 to 0.
count = 10
while count >= 0:
    print(count, end=" ")
    count -= 1
print()

# 2. Ask repeatedly for a password until the correct password is entered.
correct_password = "letmein"

entered_password = input("Enter password: ")
while entered_password != correct_password:
    print("Incorrect password, try again.")
    entered_password = input("Enter password: ")

print("Access granted.")

# 3. Create a menu that repeats until the user chooses 'quit'.
# The menu simply prints which option was selected.
choice = ""
options = ["view", "settings", "help", "quit"]
menu = "\nMenu: " + ", ".join(options)
while choice != "quit":
    print(menu)
    choice = input("Choose an option: ").strip().lower()

    if choice == "quit":
        print("Exiting menu.")
    elif choice not in options:
        print("No such option.")
    else:
        print("You selected:", choice)

# 4. Ask the user for numbers until they enter 0. Keep a running total.
running_total = 0
current_number = int(input("Enter a number (0 to stop): "))
while current_number != 0:
    running_total += current_number
    current_number = int(input("Enter a number (0 to stop): "))

print("Running total:", running_total)

# 5. Create a guessing loop with a fixed secret number. Tell the user
# whether each guess is too high or too low.
secret_number = 42

guess = int(input("Guess the number: "))
while guess != secret_number:
    if guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess the number: "))

print("Correct! The number was", secret_number)
