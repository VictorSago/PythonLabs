
# ==========================================================
# PART F - Applied challenge: Event registration processor
# ==========================================================

# 1. Core functions: normalize name, validate age, calculate fee,
# create participant dictionary.

def normalize_participant_name(name):
    # Trim stray whitespace and use consistent title-case formatting,
    return name.strip().title()


def validate_age_range(age, minimum_age=16, maximum_age=100):
    return minimum_age <= age <= maximum_age


def calculate_registration_fee(age, is_student):
    if is_student:
        base_fee = 20
    elif age >= 65:
        base_fee = 25
    else:
        base_fee = 30
    return base_fee


def create_participant(name, age, is_student):
    return {
        "name": normalize_participant_name(name),
        "age": age,
        "is_student": is_student,
        "fee": calculate_registration_fee(age, is_student),
    }


def register_participant(name, age, is_student):
    # A thin "gatekeeper" that uses validate_age_range() before
    # committing to create_participant() - kept separate from the
    # calculation functions themselves, since this is really an
    # input-handling decision (accept/reject), not a calculation.
    if not validate_age_range(age):
        print(f"Registration rejected for {name}: age {age} is outside the allowed range.")
        return None
    return create_participant(name, age, is_student)


# 2. Create at least eight participant dictionaries
participants = [
    create_participant("alice smith", 22, True),
    create_participant("Bob Traveller", 34, False),
    create_participant("  charles diaz ", 19, True),
    create_participant("Diana Chen", 45, False),
    create_participant("eva mala", 67, False),
    create_participant("Frank Lee", 20, True),
    create_participant("grace hopper", 30, False),
    create_participant("Henry Nothere", 71, False),
]


# 3. Total expected registration revenue.
def calculate_total_revenue(participant_list):
    total = 0
    for participant in participant_list:
        total += participant["fee"]
    return total


# 4. Only student participants.
def get_student_participants(participant_list):
    students = []
    for participant in participant_list:
        if participant["is_student"]:
            students.append(participant)
    return students


# 5. Oldest participant (manual search, no max()).
def get_oldest_participant(participant_list):
    oldest = participant_list[0]
    for participant in participant_list:
        if participant["age"] > oldest["age"]:
            oldest = participant
    return oldest


# 6. Readable summary string for one participant.
def summarize_participant(participant):
    student_label = "Student" if participant["is_student"] else "Non-student"
    return f"{participant['name']} (age {participant['age']}, {student_label}) - fee: €{participant['fee']}"


# 7. Keep input/output separate from calculation - a small "main-like"
# section is the only place that actually prints anything. Every
# function above returns a value and performs no printing itself.
def main():
    print("--- Age Validation ---")
    # A participant who falls outside the default 16-100 range
    attempt = register_participant("Young Kid", 12, True)
    print("Result:", attempt)

    # A participant who falls inside the range, for contrast
    attempt = register_participant("Older Adult", 55, False)
    print("Result:", attempt)
    
    if attempt:
        participants.append(attempt)

    print("--- Participants ---")
    for participant in participants:
        print(summarize_participant(participant))

    print("\n--- Revenue ---")
    print("Total expected revenue:", calculate_total_revenue(participants))

    print("\n--- Students ---")
    for student in get_student_participants(participants):
        print(summarize_participant(student))

    print("\n--- Oldest participant ---")
    print(summarize_participant(get_oldest_participant(participants)))


main()
