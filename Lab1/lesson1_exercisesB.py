
# ==========================================================
# Part B - User input and calculations
# ==========================================================

from datetime import date

# 1. Build a small profile program that asks for name and year of birth, 
# then prints an approximate age using the current year supplied in a variable.
# Instead of using a variable for the current year, we'll retrieve it with Python.
name = input("Your name: ")
year_of_birth = int(input("Year of your birth: "))
current_year = date.today().year
print("Your approximate age is: ", current_year - year_of_birth)
print()

# 2. Ask the user for the price of an item and a discount percentage, then
# calculate and print the final price rounding the displayed result to two decimals.
orig_price = float(input("Item price: "))
discount = float(input("Discount in %: "))
final_price = orig_price - (discount * orig_price) / 100
print(f"Final price: {final_price:.2f}")
print()

# 3. Ask for a temperature in Celsius and convert it to Fahrenheit.
temp_in_celsius = float(input("Temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {temp_in_celsius * 9 / 5 + 32}")
print()

# 4. Ask for the length and width of a room and calculate area and perimeter.
room_length = float(input("Room length: "))
room_width = float(input("Room width: "))
room_area = room_length * room_width
room_perimeter = 2 * room_length + 2 * room_width
print(f"Room area is {room_area}, and the perimeter is {room_perimeter}")

# 5. Extend one of the programs so invalid numeric input is discussed in comments: 
# what would happen today if the user entered "hello"?
# If the input to one of these programs had been "hello" (except for the first
# input asking for a name) the program would stop execution and exit with a "ValueError".
