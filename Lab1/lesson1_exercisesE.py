
# ==========================================================
# Part E - Applied challenge: Registration summary
# ==========================================================

# 1. Build a console program that collects first name, last name, city, 
# year of birth and favourite programming language.
# 2. Normalize text input so accidental surrounding spaces do not affect the result.
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
city = input("City: ").strip()
year_of_birth = int(input("Year of Birth: ").strip())
fav_lang = input("Favourite language: ").strip()

# 3. Create a generated user ID from parts of the person's name and year of birth.
generated_userid = first_name + last_name + str(year_of_birth)
print("Generated user ID:", generated_userid)
# 4. Print a clean multi-line summary using f-strings.
print(f" First Name: {first_name}\n"
      f" Last Name: {last_name}\n"
      f" City: {city}\n"
      f" Birth: {year_of_birth}\n"
      f" Favourite Language: {fav_lang}")

# 5. Print the initials, full name length excluding the space, and the favourite language reversed.
print(f"Initials: {first_name[0]}.{last_name[0]}.")
print(len(first_name) + len(last_name))
print(fav_lang[::-1])

# 6. Add at least three extra pieces of derived information using only concepts from Lesson 1.
city_uppercase = city.upper()
language_code = fav_lang[:2].upper()
birth_year_reversed = str(year_of_birth)[::-1]
print(f"City (uppercase): {city_uppercase}")
print(f"Language code: {language_code}")
print(f"Birth year reversed: {birth_year_reversed}")
