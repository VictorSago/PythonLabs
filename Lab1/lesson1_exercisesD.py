
# ==========================================================
# Part D - String investigation
# ==========================================================

# 1. Predict the output of at least eight expressions using indexing and slicing before running them.
some_sentence = "A long sentence with many words."
print(some_sentence[:])             # prints the whole string
print(some_sentence[2:6])           # prints the word 'long'
print(some_sentence[-6:])           # prints the last 6 characters: 'words.'
print(some_sentence[::-1])          # prints the whole string reversed
print(some_sentence[::3])           # prints every 3rd character
print(some_sentence[2:15])          # prints 'long sentence'
print(some_sentence[16:])           # prints 'with many words.'
print(some_sentence[-8:-12:-1])     # prints 'many' reversed
print()


# 2. Produce at least six different slices from string
# 'Artificial Intelligence' and comment what each slice means.
string_var = "Artificial Intelligence"
print(string_var[:3])       # First 3 characters
print(string_var[-3:])      # Last 3 characters
print(string_var[1:9])      # Characters from 1 inclusive to 9 exclusive - 8 characters
print(string_var[::5])      # Every 5 character
print(string_var[-1:0:-1])  # Reversed string except the first character
print(string_var[4::3])     # Every 3rd character from 4th to last
print()


# 3. Investigate the difference between .split(), .strip(), .replace() and the in operator. Write one useful example of each.
print(string_var.split())
print(" Hello!   ".strip())
print(string_var.replace("Intelligence", "Stupidity"))
print("a" in string_var, "z" in string_var)
print()


# 4. Demonstrate string immutability: attempt conceptually to change one
# character, explain why direct character assignment fails, then create a
# new modified string instead.

# This will fail because strings are immutable,
# so one cannot assign values to different parts of the string.
#string_var[0] = "I"

# This will succeed because a new string is being created.
modified_string = string_var[11:] + " " + string_var[:10]
print(modified_string)
