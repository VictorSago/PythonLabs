
# 1. Loop through numbers 1-100 and stop when you reach the first
# number divisible by both 7 and 9.
for number in range(1, 101):
    if number % 7 == 0 and number % 9 == 0:
        print("First number divisible by both 7 and 9:", number)
        break

# 2. Loop through a list of strings and skip empty strings using continue.
words = ["hello", "", "world", "", "python", "code"]

for word in words:
    if word == "":
        continue
    print(word)

# 3. Search a list for a target name. Print 'found' and break when it
# appears; otherwise explain how you know it was not found.
names = ["Alice", "Bob", "Carla", "David"]
target_name = "Carla"

found = False
for name in names:
    if name == target_name:
        print("Found:", name)
        found = True
        break

# If the loop finished without hitting 'break', 'found' is still False -
# that's how we know the target was never matched.
if not found:
    print(target_name, "was not found in the list.")

# 4. Process a list of numeric values where negative values should be
# skipped and processing stops completely when the value 999 appears.
values = [5, -3, 12, 999, 7, -1, 20]

for value in values:
    if value == 999:
        print("Sentinel value 999 reached - stopping.")
        break
    if value < 0:
        continue
    print("Processing value:", value)
