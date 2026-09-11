
# Lab 3 Challenge

# Departure Data
# A list of dictionaries: one dictionary per flight, since each flight is
# a set of different fields that belong together, and the list makes it easy
# to add and remove flights later.
flights = [
    {
        "flight_number": "SK142",
        "destination": "London",
        "departure_time": "14:30",
        "gate": "B4",
        "passengers": 132,
        "max_capacity": 180,
        "delay_minutes": 25,
        "cancelled": False
    },
    {
        "flight_number": "LH231",
        "destination": "Berlin",
        "departure_time": "15:00",
        "gate": "A2",
        "passengers": 98,
        "max_capacity": 150,
        "delay_minutes": 0,
        "cancelled": False
    },
    {
        "flight_number": "BA442",
        "destination": "Manchester",
        "departure_time": "15:20",
        "gate": "C1",
        "passengers": 60,
        "max_capacity": 140,
        "delay_minutes": 0,
        "cancelled": True
    },
    {
        "flight_number": "AF118",
        "destination": "Paris",
        "departure_time": "15:45",
        "gate": "A4",
        "passengers": 145,
        "max_capacity": 160,
        "delay_minutes": 10,
        "cancelled": False
    },
    {
        "flight_number": "KL876",
        "destination": "Amsterdam",
        "departure_time": "16:00",
        "gate": "B1",
        "passengers": 120,
        "max_capacity": 150,
        "delay_minutes": 70,
        "cancelled": False
    },
    {
        "flight_number": "IB305",
        "destination": "Madrid",
        "departure_time": "16:20",
        "gate": "C3",
        "passengers": 176,
        "max_capacity": 180,
        "delay_minutes": 0,
        "cancelled": False
    },
    {
        "flight_number": "LX99",
        "destination": "Zurich",
        "departure_time": "16:40",
        "gate": "A1",
        "passengers": 40,
        "max_capacity": 120,
        "delay_minutes": 0,
        "cancelled": False
    },
    {
        "flight_number": "SN201",
        "destination": "Brussels",
        "departure_time": "17:00",
        "gate": None,
        "passengers": 0,
        "max_capacity": 130,
        "delay_minutes": 10,
        "cancelled": False
    },
    {
        "flight_number": "OS455",
        "destination": "Vienna",
        "departure_time": "17:15",
        "gate": "B3",
        "passengers": 110,
        "max_capacity": 150,
        "delay_minutes": 35,
        "cancelled": False
    },
    {
        "flight_number": "TP620",
        "destination": "Lisbon",
        "departure_time": "17:30",
        "gate": "C2",
        "passengers": 88,
        "max_capacity": 140,
        "delay_minutes": 15,
        "cancelled": False
    }
]

# Gate overview
terminal_letters = ["A", "B", "C"]
gate_numbers = range(1, 5)

for terminal in terminal_letters:
    for gate_number in gate_numbers:
        print(f"Gate {terminal}{gate_number}")


# Precompute flight statistics once, before the menu starts
flight_stats = {
    "total_scheduled": len(flights),
    "cancelled": 0,
    "delayed": 0,
    "on_time": 0,
    "total_passengers": 0,
    "over_capacity": [],
    "busiest": None,
    "empty_flights": 0,
    "avg_passengers": 0,
    "total_delay_minutes": 0,
    "avg_delay": 0
}

# Calculate all the relevant statistics
for flight in flights:
    # Status (computed once, stored on the flight itself)
    if flight["cancelled"]:
        flight["status"] = "CANCELLED"
        flight_stats["cancelled"] += 1
    elif flight["delay_minutes"] >= 1:
        flight_stats["delayed"] += 1
        flight_stats["total_delay_minutes"] += flight["delay_minutes"]
        if flight["delay_minutes"] >= 60:
            flight["status"] = "SEVERELY DELAYED"
        elif flight["delay_minutes"] >= 20:
            flight["status"] = "DELAYED"
        else:
            flight["status"] = "SLIGHT DELAY"
    else:
        flight["status"] = "ON TIME"
        flight_stats["on_time"] += 1

    # Gate display (computed once, stored on the flight itself)
    flight["gate_display"] = flight["gate"] if flight["gate"] is not None else "Gate not assigned"

    # Skip 0-passenger flights when building the "active" average -
    # continue is used here because there's nothing to add
    if flight["passengers"] == 0:
        flight_stats["empty_flights"] += 1
        continue
    
    flight_stats["total_passengers"] += flight["passengers"]

    if flight["passengers"] / flight["max_capacity"] > 0.8:
        flight_stats["over_capacity"].append(flight)
    
    busiest_unset = flight_stats["busiest"] is None
    if busiest_unset or flight["passengers"] > flight_stats["busiest"]["passengers"]:
        flight_stats["busiest"] = flight

# To make calculation of average passengers easier
active_flights = flight_stats["total_scheduled"] - flight_stats["empty_flights"]

if active_flights != 0:
    flight_stats["avg_passengers"] = flight_stats["total_passengers"] / active_flights

if flight_stats["delayed"] > 0:
    flight_stats["avg_delay"] = flight_stats["total_delay_minutes"] / flight_stats["delayed"]


# Menu loop
menu_choice = ""

while True:
    print("\nAIRPORT DEPARTURE SYSTEM\n")
    print("1. View all flights")
    print("2. View delayed flights")
    print("3. View cancelled flights")
    print("4. Search for a flight")
    print("5. View flight statistics")
    print("6. Quit")
    print()
    menu_choice = input("Choose an option: ").strip()

    if menu_choice == "6":
        print("Goodbye!")
        break  # done - exit the menu loop entirely

    if menu_choice == "1":
        for flight_index, flight in enumerate(flights, start=1):
            print(
                f"{flight_index}. {flight['flight_number']} - {flight['destination']} - "
                f"{flight['departure_time']} - {flight['gate_display']} - {flight['status']}"
            )
        continue

    if menu_choice == "2":
        for flight in flights:
            # cancelled flights are never "delayed"
            if flight["cancelled"] or flight["delay_minutes"] == 0:
                continue  

            print(f"{flight['flight_number']} - {flight['destination']} - "
                  f"{flight['departure_time']} - {flight['gate']} - {flight['status']}")
        continue

    if menu_choice == "3":
        for flight in flights:
            if not flight["cancelled"]:
                continue
            print(f"{flight['flight_number']} - {flight['destination']} - CANCELLED")
        continue

    if menu_choice == "4":
        searched_flight_number = input("Enter flight number: ")

        found_flight = None
        for flight in flights:
            if flight["flight_number"] == searched_flight_number:
                found_flight = flight
                break  # stop searching once found

        if found_flight is not None:
            print()
            print("Destination:", found_flight["destination"])
            print("Departure:", found_flight["departure_time"])
            print("Gate:", found_flight['gate'])
            print("Passengers:", found_flight["passengers"])
            print("Status:", found_flight['status'])
        else:
            print("Flight not found.")
        continue

    if menu_choice == "5":
        busiest = flight_stats["busiest"]
        print()
        print("Total scheduled flights:", flight_stats["total_scheduled"])
        print("Cancelled flights:", flight_stats["cancelled"])
        print("Delayed flights:", flight_stats["delayed"])
        print("On-time flights:", flight_stats["on_time"])
        print("Total passengers:", flight_stats["total_passengers"])
        print("Average passengers:", round(flight_stats["avg_passengers"], 2))
        print(f"Busiest flight: {busiest['flight_number']} - {busiest['destination']} - "
              f"{busiest['passengers']} passengers")
        print("Flights above 80% capacity:", len(flight_stats["over_capacity"]))
        continue

    print("Invalid option, please choose 1-6.")

busiest = flight_stats["busiest"]

print("\nAIRPORT OPERATIONS REPORT\n")
print("Scheduled flights:", flight_stats["total_scheduled"])
print("Cancelled flights:", flight_stats["cancelled"])
print("Delayed flights:", flight_stats["delayed"])
print("On-time flights:", flight_stats["on_time"])
print()
print("Passengers today:", flight_stats["total_passengers"])
print()
print("Busiest flight:")
print(f"{busiest['flight_number']} - {busiest['destination']} - {busiest['passengers']} passengers")
print()
print("Flights above 80% capacity:")
for flight in flight_stats["over_capacity"]:
    print(f"{flight['flight_number']} - {flight['destination']}")
print()
# Additional analysis: average delay among delayed flights
print("Average delay (delayed flights only):", round(flight_stats["avg_delay"], 2), "minutes")


# ==========================================================
# Part 9 - Control the processing (review)
# ==========================================================
# 
# break usage:
# - Menu option 4 (search): breaks out of the search loop as soon as the
#   matching flight is found. Purpose: there's only ever one flight with
#   a given flight number, so continuing to scan the rest of the list after
#   a match is pure wasted work.
# - The menu loop itself breaks out when the user chooses "6". Purpose: this 
#   is the only way to end an infinite `while True` menu loop - without it
#   the program could never exit.
#
# continue usage:
# - The stats-gathering loop: `continue` skips a flight with 0 passengers
#   before modifying the `total_passengers` count, determining overcapacity,
#   or comparing with the busiest flight. Purpose: those lines don't apply to
#   a 0-passenger flight.
# - Every branch of the menu loop ends in `continue`. Purpose: after handling
#   one menu option, control should go straight back to showing the menu again 
#   rather than falling through to the "invalid option" message at the bottom.

# ==========================================================
# DESIGN CHALLENGE
# ==========================================================
# 
# Improvement 1
# What the original solution did:
#   Tracked flight statistics as several separate loose variables 
#   (total_scheduled_flights, cancelled_count, delayed_count, etc.)
# What was changed:
#   Consolidated all of these into a single flight_stats dictionary,
#   and replaced active_passenger_flight_count with a more meaningful
#   empty_flights counter (flights - empty_flights = active flights).
# Why the new solution is better:
#   One named collection instead of many loose variables is easier to 
#   keep track of, print, and extend later (e.g. adding avg_delay
#   for the last part of the lab). empty_flights is also a fact about the 
#   airport in its own right, whereas active_passenger_flight_count only ever
#   existed to make one division work - the new version's data
#   structure choice matches what it's actually modeling.
#
# Improvement 2
# What the original solution did:
#   Menu option 1 (view all flights) and option 4 (search) each
#   independently recomputed a flight's status (CANCELLED / SEVERELY
#   DELAYED / DELAYED / SLIGHT DELAY / ON TIME) and gate display
#   ("Gate not assigned" fallback) using the same if/elif chain,
#   duplicated verbatim in two places.
# What was changed:
#   Computed status and gate_display once per flight during the initial stats
#   loop, storing them directly as extra keys on each flight's dictionary 
#   (`flight["status"]`, `flight["gate_display"]`). Menu options 1 and 4 now
#   just read these values from flight's `dict` instead of recalculating them.
# Why the new solution is better:
#   Removes unnecessary repetition - the status rules are now written in
#   exactly one place, so a future rule change only needs to happen once 
#   instead of being kept in sync across every place status is displayed. 
#   It also avoids unnecessary processing, since a flight's status/gate
#   display no longer gets recomputed from scratch every time.
