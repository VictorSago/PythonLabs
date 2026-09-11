
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
    "over_capacity": 0,
    "busiest": None,
    "empty_flights": 0,
    "avg_passengers": 0,
}

# For the average, only "active" flights count


for flight in flights:
    if flight["cancelled"]:
        flight_stats["cancelled"] += 1
    elif flight["delay_minutes"] > 0:
        flight_stats["delayed"] += 1
    else:
        flight_stats["on_time"] += 1
    
    # Skip 0-passenger flights when building the "active" average -
    # continue is used here because there's nothing to add
    if flight["passengers"] == 0:
        flight_stats["empty_flights"] += 1
        continue
    
    flight_stats["total_passengers"] += flight["passengers"]

    if flight["passengers"] / flight["max_capacity"] > 0.8:
        flight_stats["over_capacity"] += 1
    
    busiest_unset = flight_stats["busiest"] is None
    if busiest_unset or flight["passengers"] > flight_stats["busiest"]["passengers"]:
        flight_stats["busiest"] = flight

active_flights = flight_stats["total_scheduled"] - flight_stats["empty_flights"]
if active_flights != 0:
    flight_stats["avg_passengers"] = flight_stats["total_passengers"] / active_flights

# --- Menu loop ---
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
            if flight["cancelled"]:
                status = "CANCELLED"
            elif flight["delay_minutes"] >= 60:
                status = "SEVERELY DELAYED"
            elif flight["delay_minutes"] >= 20:
                status = "DELAYED"
            elif flight["delay_minutes"] >= 1:
                status = "SLIGHT DELAY"
            else:
                status = "ON TIME"

            gate_display = flight["gate"] if flight["gate"] is not None else "Gate not assigned"

            print(
                f"{flight_index}. {flight['flight_number']} - {flight['destination']} - "
                f"{flight['departure_time']} - {gate_display} - {status}"
            )
        continue

    if menu_choice == "2":
        for flight in flights:
            if flight["cancelled"]:
                continue  # cancelled flights are never "delayed"
            if flight["delay_minutes"] == 0:
                continue  # nothing to show in a delayed-only view

            if flight["delay_minutes"] >= 60:
                status = "SEVERELY DELAYED"
            elif flight["delay_minutes"] >= 20:
                status = "DELAYED"
            else:
                status = "SLIGHT DELAY"
            
            gate_display = flight["gate"] if flight["gate"] is not None else "Gate not assigned"

            print(f"{flight['flight_number']} - {flight['destination']} - "
                  f"{flight['departure_time']} - {gate_display} - {status}")
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
            gate_display = (
                found_flight["gate"] if found_flight["gate"] is not None else "Gate not assigned"
            )

            if found_flight["cancelled"]:
                status = "CANCELLED"
            elif found_flight["delay_minutes"] >= 60:
                status = "SEVERELY DELAYED"
            elif found_flight["delay_minutes"] >= 20:
                status = "DELAYED"
            elif found_flight["delay_minutes"] >= 1:
                status = "SLIGHT DELAY"
            else:
                status = "ON TIME"

            print()
            print("Destination:", found_flight["destination"])
            print("Departure:", found_flight["departure_time"])
            print("Gate:", gate_display)
            print("Passengers:", found_flight["passengers"])
            print("Status:", status)
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
        print("Flights above 80% capacity:", flight_stats["over_capacity"])
        continue

    print("Invalid option, please choose 1-6.")

