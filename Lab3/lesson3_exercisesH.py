
# 1. Print FizzBuzz from 1 to 100:
# multiples of 3 -> Fizz, 5 -> Buzz, both -> FizzBuzz.
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 2. Given a sentence, count vowels without using .count() repeatedly.
sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiouyAEIOUY"

vowel_count = 0
for character in sentence:
    if character in vowels:
        vowel_count += 1

print("Vowel count:", vowel_count)

# 3. Find all duplicate values in a list using loops and collections.
values = [4, 8, 15, 16, 23, 4, 8, 42, 15, 4]

seen = set()
duplicates = set()

for value in values:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)

print("Duplicate values:", duplicates)

# 4. Build a simple text histogram: for each number in [3, 5, 2],
# print that many * characters.
bar_lengths = [3, 5, 2]

for num in bar_lengths:
    bar = "*" * num
    print(bar)
