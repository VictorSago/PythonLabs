
# ==========================================================
# Part G - Stretch challenges
# ==========================================================

# 1. Return both minimum and maximum from a list. Return two values.
def find_min_and_max(numbers: list) -> tuple:
    """Return the smallest and largest numbers in the list as a tuple."""
    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return smallest, largest


# lowest, highest = find_min_and_max([7, 2, 9, 4, 1, 8])
# print(f"Min: {lowest}, Max: {highest}")

# 2. Check whether a word is a palindrome.
def is_palindrome(word: str) -> bool:
    """Return True if word reads the same forwards and backwards."""
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]


# print(is_palindrome("racecar"))
# print(is_palindrome("python"))
# print(is_palindrome("Level"))

# 3. Count character frequencies and return a dictionary.
def count_character_frequencies(text: str) -> dict:
    """Return a dictionary mapping each character in text to its count."""
    frequencies = {}
    for character in text:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
    return frequencies


# print(count_character_frequencies("banana"))

# 4. Receive a list of numbers, return a new dictionary with keys
# positive, negative and zero containing counts.
def count_by_sign(numbers: list) -> dict:
    """Return a dict counting how many numbers are positive, negative, or zero."""
    counts = {"positive": 0, "negative": 0, "zero": 0}

    for number in numbers:
        if number > 0:
            counts["positive"] += 1
        elif number < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1

    return counts


# print(count_by_sign([4, -2, 0, 7, -9, 0, 3]))

# 5. Light type hints and a short docstring on at least five functions.
# All four functions above already include type hints and a one-line 
# docstring. Here's a fifth, reusing an earlier function from Part F
# to complete the count:
def summarize_participant(participant: dict) -> str:
    """Return a readable one-line summary of a single participant."""
    student_label = "Student" if participant["is_student"] else "Non-student"
    return f"{participant['name']} (age {participant['age']}, {student_label}) - fee: ${participant['fee']}"


# ============================================================
# PART G - main() section
# ============================================================

def main():
    print("--- Min and Max ---")
    lowest, highest = find_min_and_max([7, 2, 9, 4, 1, 8])
    print(f"Min: {lowest}, Max: {highest}")

    print("\n--- Palindrome Check ---")
    print("racecar:", is_palindrome("racecar"))
    print("python:", is_palindrome("python"))
    print("Level:", is_palindrome("Level"))

    print("\n--- Character Frequencies ---")
    print(count_character_frequencies("banana"))

    print("\n--- Count by Sign ---")
    print(count_by_sign([4, -2, 0, 7, -9, 0, 3]))

    print("\n--- Participant Summaries ---")
    # Built using create_participant() from Part F, so the data going
    # into summarize_participant() is consistent with how participants
    # are created everywhere else in this file.
    stretch_participants = [
        {
            "name": "Alice",
            "age": 36,
            "is_student": True,
            "fee": 20
        },
        {
            "name": "Zaphod",
            "age": 442,
            "is_student": False,
            "fee": 30
        },
        {
            "name": "Ada",
            "age": 42,
            "is_student": False,
            "fee": 25
        }
    ]
    for participant in stretch_participants:
        print(summarize_participant(participant))


main()
