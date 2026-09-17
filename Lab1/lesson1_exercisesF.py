
# ==========================================================
# Part F - Stretch challenges Python Foundation
# ==========================================================

# Ex 1
total_seconds = int(input("Total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

print()

# Ex 2
number = 2468
print("Full number:", number)
print(f"First: {number // 1000}, Second: {number % 1000 // 100}")
print(f"Third: {number % 100 // 10}, Fourth: {number % 10}")
print()

# Ex 3
supplied_word = "SomeLongWord"
print(supplied_word[:2] + "*" * (len(supplied_word) - 4) + supplied_word[-2:])
print()

# Ex 4
