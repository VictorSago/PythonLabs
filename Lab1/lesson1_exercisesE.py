
# ==========================================================
# Part E - Applied challenge: Registration summary
# ==========================================================

first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
city = input("City: ").strip()
year_of_birth = int(input("Year of Birth: ").strip())
fav_lang = input("Favourite language: ").strip()
gen_user_id = first_name + last_name + str(year_of_birth)
print("Generated user ID:", gen_user_id)
print(f" First Name: {first_name}\n"
      f" Last Name: {last_name}\n"
      f" City: {city}\n"
      f" Birth: {year_of_birth}\n"
      f" Favourite Language: {fav_lang}")
print(f"Initials: {first_name[0]}.{last_name[0]}.")
print(len(first_name) + len(last_name))
print(fav_lang[::-1])

# Ex 6
