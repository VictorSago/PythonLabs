
# 1. Use range to print 10 down to 1.
for number in range(10, 0, -1):
    print(number)

# 2. Generate the multiplication table for a number supplied by the user.
table_number = int(input("Enter a number for its multiplication table: "))

for multiplier in range(1, 11):
    print(f"{table_number} x {multiplier} = {table_number * multiplier}")

# 3. Use enumerate to print a playlist with track numbers starting at 1.
playlist = ["Bohemian Rhapsody", "Imagine", "Hotel California", "Yesterday"]

for track_number, song in enumerate(playlist, start=1):
    print(f"{track_number}. {song}")

# 4. Use nested loops to print coordinate pairs for x=1..3 and y=1..4.
for x in range(1, 4):
    for y in range(1, 5):
        print(f"({x}, {y})")

# 5. Create a simple 5x5 text grid using nested loops.
for row in range(5):
    line = ""
    for column in range(5):
        line += "* "
    print(line)
