
# ==========================================================
# Part 1 - Design the conference data
# ==========================================================

# Speakers are represented by dictionaries because the fields defining a speaker belong together.
# Skills are a set because for each participant a skill should only appear once.
speakers = [
    {"name": "Ada Lovelace", "skills": {"Programming", "Mathematics", "Algorithms"}},
    {"name": "Grace Hopper", "skills": {"Python", "Compilers", "COBOL"}},
    {"name": "Alan Turing", "skills": {"Algorithms", "Cryptography", "AI"}},
    {"name": "Alonzo Church", "skills": {"Mathematics", "Python", "Programming"}},
    {"name": "Tim Berners-Lee", "skills": {"Web", "Networking", "APIs"}},
]

# Rooms are a plain list because some rooms might be added or removed.
rooms = ["Room A", "Room B", "Room C", "Room D"]

# Topics/categories are a set because duplicates don't make sense.
topics = {"AI", "Web Development", "Data Science", "Programming Languages", "Programming"}

# Participants are a list of dictionaries, 
# so it can grow (with registrations) or shrink (with cancellations).
# Each participant is a dict of properties belongiong together.
participants = [
    {"name": "Alice Smith", "email": "alice@example.com"},
    {"name": "Bob Joneson", "email": "bob@example.com"},
    {"name": "Charles Babbage", "email": "charles@example.com"},
    {"name": "David Hilbert", "email": "david@example.com"},
    {"name": "Eve Mala", "email": "eva@example.com"},
    {"name": "Frank Enigma", "email": "frank@example.com"},
    {"name": "Grace Kim", "email": "grace@example.com"},
    {"name": "Henry Polymath", "email": "hassan@example.com"},
    {"name": "Irene Descartes", "email": "irene@example.com"},
    {"name": "Jack New", "email": "jack@example.com"},
]

# Sessions is a list of dictionaries because we'll have to mutate and slice it.
# Each session is a dict grouping its different properties together.
# "start_time" is a tuple because (hour, minute) belong together
# and shouldn't be edited element-by-element.
sessions = [
    {
        "title": "Python for AI",
        "speaker": "Ada Lovelace",
        "room": "Room A",
        "start_time": (9, 0),
        "duration": 60,
        "topic": "Programming",
        "max_participants": 30,
    },
    {
        "title": "Building APIs",
        "speaker": "Tim Berners-Lee",
        "room": "Room B",
        "start_time": (9, 0),
        "duration": 45,
        "topic": "Web Development",
        "max_participants": 25,
    },
    {
        "title": "Introduction to LLMs",
        "speaker": "Alan Turing",
        "room": "Room C",
        "start_time": (10, 15),
        "duration": 60,
        "topic": "AI",
        "max_participants": 40,
    },
    {
        "title": "Data Wrangling 101",
        "speaker": "Grace Hopper",
        "room": "Room D",
        "start_time": (10, 15),
        "duration": 50,
        "topic": "Data Science",
        "max_participants": 20,
    },
    {
        "title": "Programming with Functions",
        "speaker": "Alonzo Church",
        "room": "Room A",
        "start_time": (11, 30),
        "duration": 45,
        "topic": "Programming Languages",
        "max_participants": 35,
    },
    {
        "title": "REST vs GraphQL",
        "speaker": "Tim Berners-Lee",
        "room": "Room B",
        "start_time": (13, 0),
        "duration": 60,
        "topic": "Web Development",
        "max_participants": 25,
    },
    {
        "title": "Ethics in AI",
        "speaker": "Alan Turing",
        "room": "Room C",
        "start_time": (14, 0),
        "duration": 30,
        "topic": "AI",
        "max_participants": 50,
    },
    {
        "title": "Compiler as a Metaphor",
        "speaker": "Grace Hopper",
        "room": "Room D",
        "start_time": (15, 0),
        "duration": 30,
        "topic": "Programming",
        "max_participants": 60,
    },
]

# ==========================================================
# Part 2 - Work with the schedule
# ==========================================================
print("--- Part 2 ---")

# 1. Title of the first session
print(sessions[0]["title"])
# 2. Speaker of the third session
print(sessions[2]["speaker"])
# 3. Room of the last session (negative indexing)
print(sessions[-1]["room"])
# 4. All info about one selected session
print(sessions[4])
# 5. One specific value from a nested structure using chained indexing
# (the minute component of the third session's start_time tuple)
print(sessions[2]["start_time"][1])
# 6. First three sessions (slicing)
print(sessions[0:3])
# 7. Last two sessions (slicing)
print(sessions[-2:])
# 8. Reversed version of the session schedule (slicing with step -1)
reversed_sessions = sessions[::-1]
print(reversed_sessions)
# 9. A copy containing only part of the schedule (e.g. sessions 2-5)
partial_schedule = sessions[2:5]
print(partial_schedule)
print()

# ==========================================================
# Part 3 - Conference changes
# ==========================================================
print("--- Part 3 ---")

# --- Show state before changes ---
print("\n--- Before ---")
print("Session 1 room:", sessions[0]["room"])
print("Session 2 speaker:", sessions[1]["speaker"])
print("Number of sessions:", len(sessions))
print("Participants:", len(participants))
print("Participant list:", participants)

# 1. One session changes room
sessions[0]["room"] = "Room D"
# 2. One speaker is replaced by another speaker
sessions[1]["speaker"] = "Grace Hopper"
# 3. A new session is added
sessions.append(
    {
        "title": "Intro to Quantum Computing",
        "speaker": "Alan Turing",
        "room": "Room B",
        "start_time": (16, 0),
        "duration": 45,
        "topic": "AI",
        "max_participants": 30,
    }
)

print("\n--- After Adding a Session ---")
print("Session 1 room:", sessions[0]["room"])
print("Session 2 speaker:", sessions[1]["speaker"])
print("Number of sessions:", len(sessions))
print("Last session added:", sessions[-1])

# 4. One session is cancelled and removed (removing 2nd session in the list).
# Could use `del session[1]` but can't remember whether the lesson covered it.
temp_session = sessions.pop(1)

print("\n--- After Removing a Session ---")
print("Number of sessions:", len(sessions))
print("Removed session:", temp_session)
print("Sessions in the list:", sessions)

# 5. One participant registers for the conference
participants.append({"name": "Karen Clueless", "email": "karen@example.com"})
# 6. One participant cancels their registration
participants.pop(0)  # Alice Smith cancels
# 7. One session receives an additional piece of information: difficulty
sessions[2]["difficulty"] = "Intermediate"

# --- Show state after changes ---
print("\n--- After All Changes ---")
print("Session 3 difficulty:", sessions[2]["difficulty"])
print("Participants:", len(participants))
print("Participant list:", participants)
print()

# ==========================================================
# Part 4 - Unique conference information
# ==========================================================
print("--- Part 4 ---")

# Unique conference topics (already defined in Part 1 as a set)
print("Unique topics:", topics)

# Unique technical skills represented by speakers
# Combine all speaker skill sets using the union operator.
all_speaker_skills = (
    speakers[0]["skills"]
    | speakers[1]["skills"]
    | speakers[2]["skills"]
    | speakers[3]["skills"]
    | speakers[4]["skills"]
)
print("Unique skills across all speakers:", all_speaker_skills)

# --- Workshop registrations ---
# Sets of participant names registered for each of two workshops.
# A set is appropriate because what matters is whether 
# a participant is in workshop or not.
workshop_a = {"Bob Joneson", "Charles Babbage", "David Hilbert", "Eve Mala", "Frank Enigma"}
workshop_b = {"David Hilbert", "Eve Mala", "Grace Kim", "Henry Polymath", "Karen Clueless"}

print("Workshop A participants:", workshop_a)
print("Workshop B participants:", workshop_b)

# Participants registered for both workshops (intersection)
both_workshops = workshop_a & workshop_b
print("Registered for both workshops:", both_workshops)
# Participants registered only for Workshop A (difference)
only_workshop_a = workshop_a - workshop_b
print("Registered only for Workshop A:", only_workshop_a)
# Participants registered only for Workshop B (difference)
only_workshop_b = workshop_b - workshop_a
print("Registered only for Workshop B:", only_workshop_b)
# All unique participants registered for either workshop (union)
any_workshop = workshop_a | workshop_b
print("Registered for either workshop:", any_workshop)
print()

# ==========================================================
# Part 5 - Conference configuration
# ==========================================================
print("--- Part 5 ---")

# Fixed, related values that belong together and shouldn't normally
# change piece-by-piece -> tuples are the right fit here.

# Conference dates (start date, end date) - a fixed pair
conference_dates = ("2026-11-10", "2026-11-11")

# Opening and closing times (hour, minute) each day
opening_time = (9, 0)
closing_time = (17, 30)

# Conference contact information (name, email, phone) - fixed together
conference_contact = ("Conference Office", "info@techconf.example.com", "+46-8-555-1100")

# --- Access individual values ---
print("Conference starts on:", conference_dates[0])
print("Conference ends on:", conference_dates[1])
print("Opening hour:", opening_time[0])
print("Closing minute:", closing_time[1])
print("Contact email:", conference_contact[1])

# --- Unpack one of them into separate variables ---
contact_name, contact_email, contact_phone = conference_contact
print("Contact name:", contact_name)
print("Contact email:", contact_email)
print("Contact phone:", contact_phone)

start_date, end_date = conference_dates
print("Runs from", start_date, "to", end_date)
print()

# ==========================================================
# Part 6 - The shared-reference problem
# ==========================================================
print("--- Part 6 ---")

# Start with the existing participant list
backup_participants = participants

# Modify the backup
backup_participants.append({"name": "Arthur Dent", "email": "arthur@example.com"})

# Print both variables
print("participants:", participants)
print("backup_participants:", backup_participants)

# What happened?
# 'backup_participants = participants' does not create a new list -
# it just makes 'backup_participants' another name (reference) that
# points to the *same* list object in memory. Lists are mutable, so
# any change made through either name modifies the one underlying
# object both variables refer to. There is only one list; two labels.

# .copy() creates a new, independent list object with the same elements.
safe_backup_participants = participants.copy()

# Modify only the safe backup
safe_backup_participants.append({"name": "Zaphod Beeblebrox", "email": "zaphod@example.com"})

# Demonstrate that the original list was NOT affected this time
print("\nAfter using .copy():")
print("participants:", participants)
print("safe_backup_participants:", safe_backup_participants)
print("Same object?", participants is safe_backup_participants)  # False
print("Different lengths:", len(participants), "vs", len(safe_backup_participants))
print()

# ==========================================================
# Extra challenge - What happens when the list contains dictionaries
# and we use .copy()?
# ==========================================================
print("--- Extra ---")

# Reuse safe_backup_participants from Part 6, which was created with
# participants.copy()
# Change a value inside one of the dictionaries in the copied list
safe_backup_participants[0]["email"] = "changed_email@example.com"

# Does the original data change?
print("Original participants[0]:", participants[0])
print("Copied safe_backup_participants[0]:", safe_backup_participants[0])
print("Same dict object?", participants[0] is safe_backup_participants[0])  # True

# Explanation:
# Yes - the original dictionary's email also changed, even though we
# only used .copy() and only modified the "copy".
#
# list.copy() performs a SHALLOW copy: it creates a new list object,
# but the *elements inside* that list are not copied themselves - the
# new list just stores references to the exact same dictionary objects
# as the original list. So participants[0] and safe_backup_participants[0]
# are two different list slots pointing at one and the same dictionary
# in memory. Changing a value inside that dictionary is visible through
# either list, because there is still only one dictionary.
#
# This can be solved with .deepcopy() which
# recursively copies nested objects too, not just the outer list.
print()

# ==========================================================
# Part 7 - Restructure the data
# ==========================================================
print("--- Part 7 ---")

# unrelated lists:
session_titles = [
    "Python for AI",
    "Building APIs",
    "Introduction to LLMs",
]
speakers_flat = [
    "Ada",
    "Grace",
    "Alan",
]
rooms_flat = [
    "Room A",
    "Room B",
    "Room C",
]

# A better, connected structure
# Each session becomes one dictionary that keeps title/speaker/room
# (and now three extra fields) together in a single place. The three
# sessions live in a list, since order/position still matters.
restructured_sessions = [
    {
        "title": "Python for AI",
        "speaker": "Ada",
        "room": "Room A",
        "duration": 60,
        "topic": "AI",
        "max_participants": 30,
    },
    {
        "title": "Building APIs",
        "speaker": "Grace",
        "room": "Room B",
        "duration": 45,
        "topic": "Web Development",
        "max_participants": 25,
    },
    {
        "title": "Introduction to LLMs",
        "speaker": "Alan",
        "room": "Room C",
        "duration": 60,
        "topic": "AI",
        "max_participants": 40,
    },
]

# Demonstrate access to the second session's title, speaker, room
print("Second session's title:", restructured_sessions[1]["title"])
print("Second session's speaker:", restructured_sessions[1]["speaker"])
print("Second session's room:", restructured_sessions[1]["room"])

# Why this structure is easier to work with than several separate lists:
# Each session is now one self-contained dictionary, so title, speaker,
# room and the extra fields can never accidentally get out of sync (e.g.
# by inserting into one list but forgetting another). Looking up "session 2"
# means a single index into one list instead of the same index into three
# different lists that all have to be kept in the same order by hand.
# It also makes it trivial to add/remove a whole session as one unit
# (append/remove one dict) rather than having to update three lists
# together.
print()

# ==========================================================
# Final Challenge - Build the Complete Conference State
# ==========================================================
print("---Final Challenge ---")

# One unified, nested structure tying everything together:
# conference -> sessions -> speaker/room/topic, etc.
conference = {
    "name": "TechConf 2026",
    "dates": conference_dates,          # tuple (Part 5)
    "opening_time": opening_time,       # tuple (Part 5)
    "closing_time": closing_time,       # tuple (Part 5)
    "contact": conference_contact,      # tuple (Part 5)
    "sessions": sessions,               # list of dicts (Part 1/3)
    "speakers": speakers,               # list of dicts with sets (Part 1)
    "rooms": rooms,                     # list (Part 1)
    "topics": topics,                   # set (Part 1)
    "participants": participants,       # list of dicts (Part 1/3/6)
    "workshops": {                      # dict of sets (Part 4)
        "Workshop A": workshop_a,
        "Workshop B": workshop_b,
    },
}

# ----------------------------------------------------------
# Retrieve and print at least 10 pieces of information from
# different levels of the structure (at least 5 require nested access)
# ----------------------------------------------------------
print("Conference name:", conference["name"])
print("Opening time:", conference["opening_time"])
print("First session title:", conference["sessions"][0]["title"])
print("Third session speaker:", conference["sessions"][2]["speaker"])
print("First speaker's skills:", conference["speakers"][0]["skills"])
print("Last room:", conference["rooms"][-1])
print("All topics:", conference["topics"])
print("First participant:", conference["participants"][0]["name"])
print("Contact email:", conference["contact"][1])
print("Workshop A registrants:", conference["workshops"]["Workshop A"])

# ----------------------------------------------------------
# Make at least 5 changes using appropriate collection operations
# ----------------------------------------------------------

# 1. Add a new topic (set operation: add)
conference["topics"].add("Networking")
# 2. Add a new session (list operation: append)
conference["sessions"].append(
    {
        "title": "Closing Keynote",
        "speaker": "Alonzo Church",
        "room": "Room A",
        "start_time": (17, 0),
        "duration": 30,
        "topic": "Networking",
        "max_participants": 100,
    }
)
# 3. Remove a room that's no longer available (list operation: remove)
conference["rooms"].remove("Room D")
# 4. A participant cancels (list operation: pop)
conference["participants"].pop()
# 5. Give a speaker an extra skill (nested set operation: add)
conference["speakers"][0]["skills"].add("Leadership")
# Show the results of the changes
print("\n--- AFTER FINAL CHANGES ---")
print("Total sessions:", len(conference["sessions"]))
print("Last session added:", conference["sessions"][-1]["title"])
print("Topics now:", conference["topics"])
print("Rooms now:", conference["rooms"])
print("Total participants:", len(conference["participants"]))
print("First speaker's skills now:", conference["speakers"][0]["skills"])

# ==========================================================
# Design Explanation
# ==========================================================

# 10. Where did you use a list, and why was a list suitable?
#     Lists were used for `sessions`, `participants`, `rooms`, and
#     `speakers`. These are all collections where order/position
#     matters (first session, last session, second speaker) and where
#     items are regularly added or removed (new session, participant
#     registering/cancelling). Lists are mutable and preserve insertion
#     order, which is exactly what's needed here.

# 11. Where did you use a dictionary, and why was a dictionary suitable?
#     Each session, speaker, and participant is a dictionary, and the whole
#     `conference` structure itself is a dictionary. Dictionaries were
#     used because these are collections of *different, named* pieces
#     of information that belong together and are looked up by label 
#     rather than by position - far more readable than trying to remember
#     that "index 2 is always the room".

# 12. Where did you use a tuple, and why was a tuple suitable?
#     `start_time` (hour, minute), `conference_dates`, `opening_time`,
#     `closing_time`, and `conference_contact` are all tuples. These values
#     are fixed, small, and meant to be treated as a single unit that isn't
#     edited piece-by-piece after creation - a start time is always
#     "an hour and a minute together", not just two independent numbers.

# 13. Where did you use a set, and why was a set suitable?
#     `topics`, each speaker's `skills`, and the two `workshop` membership
#     groups are sets. In all three cases, order doesn't matter and duplicates
#     don't make sense (a topic shouldn't be listed twice; a participant is
#     either registered for a workshop or not). Sets also made the 
#     "both / only A / only B / either" comparisons in Part 4 trivial.

# 14. Which parts of your data are mutable?
#     `sessions`, `participants`, `rooms`, `speakers`, `topics`, the
#     workshop sets, and the dictionaries nested inside them. These
#     all change over the life of the conference: sessions get added
#     or cancelled, participants register or cancel, a speaker can
#     gain a new skill, topics can grow.

# 15. Which parts should ideally remain unchanged?
#     The tuples: `conference_dates`, `opening_time`, `closing_time`,
#     `conference_contact`, and each session's `start_time`. These
#     represent fixed facts that should be replaced wholesale if they
#     ever need to change, not edited element-by-element.

# 16. What is one advantage of using nested collections?
#     Related information stays logically grouped and travels together
#     automatically. `conference["sessions"][0]["speaker"]` reads as
#     one coherent path ("conference, then sessions, then the
#     speaker"), and copying/passing around one session dict carries
#     all of its data with it.

# 17. What is one disadvantage of deeply nested collections?
#     They get harder to read and access as nesting grows - something
#     like conference["sessions"][3]["start_time"][1] requires knowing
#     the exact shape at every level, and a typo at any step causes an error
#     or silently gets the wrong value. It also makes copying tricky.

# 18. What is the difference between assigning one list to another
#     variable and copying the list?
#     `backup_participants = participants` makes `backup` just another name
#     pointing at the exact same list object - changes through either name
#     affect the one underlying list (Part 6). 
#     `safe_backup_participants = participants.copy()` creates a genuinely new,
#     independent list object, so changes to `safe_backup_participants`'s own
#     structure do not affect `participants`. However, `.copy()` is shallow: 
#     if the list holds mutable elements like dictionaries, both lists still
#     reference the *same* inner dictionaries, so editing a value inside one
#     of those dictionaries is visible through either list.

# 19. If you were allowed to use concepts from later lessons, what part
#     of your solution would you most want to improve?
#     I'd replace the repeated, similarly-shaped session/speaker/
#     participant dictionaries with classes, which would let me validate
#     data on creation, add behaviour (like checking room capacity), and
#     avoid relying on exact string keys everywhere. I'd also use loops to 
#     build and process the data instead of writing each entry out by hand,
#     and `copy.deepcopy()` to solve the shallow-copy problem from the
#     Extra Challenge.
