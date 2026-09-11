
# 1. A list of dictionaries representing at least ten study sessions
# with subject and minutes.
study_sessions = [
    {"subject": "Math", "minutes": 30},
    {"subject": "Physics", "minutes": 50},
    {"subject": "Math", "minutes": 20},
    {"subject": "History", "minutes": 40},
    {"subject": "Physics", "minutes": 60},
    {"subject": "Programming", "minutes": 90},
    {"subject": "Math", "minutes": 45},
    {"subject": "History", "minutes": 15},
    {"subject": "Programming", "minutes": 35},
    {"subject": "Chemistry", "minutes": 25},
]

# 2. Loop through the sessions and calculate total minutes.
total_minutes = 0
for session in study_sessions:
    total_minutes += session["minutes"]

print("Total minutes studied:", total_minutes)

# 3. Calculate total minutes per subject using a dictionary that
# starts empty and is updated inside the loop.
minutes_per_subject = {}

for session in study_sessions:
    subject = session["subject"]
    minutes = session["minutes"]

    if subject in minutes_per_subject:
        minutes_per_subject[subject] += minutes
    else:
        minutes_per_subject[subject] = minutes

print("Minutes per subject:", minutes_per_subject)

# 4. Identify the longest study session without max(..., key=...).
longest_session = study_sessions[0]

for session in study_sessions:
    if session["minutes"] > longest_session["minutes"]:
        longest_session = session

print("Longest session:", longest_session)

# 5. Print only sessions longer than 45 minutes.
print("Sessions longer than 45 minutes:")
for session in study_sessions:
    if session["minutes"] > 45:
        print(f"  {session['subject']}: {session['minutes']} minutes")

# 6 & 7. A repeated menu that lets a user view all sessions, view
# total time, filter by subject, or quit - using break/continue where
# they genuinely improve the flow.
menu_choice = ""

while True:
    print("\n--- Study Tracker Menu ---")
    print("1. View all sessions")
    print("2. View total time")
    print("3. Filter by subject")
    print("4. Quit")
    menu_choice = input("Choose an option (1-4): ").strip()

    if menu_choice == "4":
        print("Goodbye!")
        break  # exit the menu loop entirely

    if menu_choice == "1":
        for session in study_sessions:
            print(f"  {session['subject']}: {session['minutes']} minutes")
        continue  # go straight back to showing the menu

    if menu_choice == "2":
        # Repeating the code from exercise 2
        total_time = 0
        for session in study_sessions:
            total_time += session["minutes"]
        print("Total time studied:", total_time, "minutes")
        continue

    if menu_choice == "3":
        subject_filter = input("Enter subject to filter by: ").strip().lower()
        for session in study_sessions:
            if session["subject"].lower() != subject_filter:
                continue  # skip sessions that don't match
            print(f"  {session['subject']}: {session['minutes']} minutes")
        continue

    # Anything that isn't 1-4 falls through to here
    print("Invalid option, please choose 1-4.")
