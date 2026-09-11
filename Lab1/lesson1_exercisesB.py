
from datetime import date

# Part B - Input and calculations

# Ex 1
name = input("Your name: ")
year_of_birth = int(input("Year of your birth: "))
print("Your approximate age is: ", date.today().year - year_of_birth)
print()

# Ex 2
orig_price = float(input("Item price: "))
discount = float(input("Discount in %: "))
final_price = (100 - discount) * orig_price / 100
print(f"Final price: {final_price:.2f}")
print()

# Ex 3
temp_in_celsius = float(input("Temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {temp_in_celsius * 9 / 5 + 32}")
print()

# Ex 4
room_length = float(input("Room length: "))
room_width = float(input("Room width: "))
room_area = room_length * room_width
room_perimeter = 2 * room_length + 2 *room_width
print(f"Room area is {room_area}, and the perimeter is {room_perimeter}")

# Ex 5
# If the input to one of these programs had been "hello" (except for the first input asking for a name)
# the program would stop execution and exit with a "ValueError".
