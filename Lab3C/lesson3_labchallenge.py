
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
        "delay_minutes": 5,
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

# Loop with enumerate so flights are numbered automatically -
for flight_number, flight in enumerate(flights, start=1):

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
        f"{flight_number}. {flight['flight_number']} - {flight['destination']} - "
        f"{flight['departure_time']} - {gate_display} - {status}"
    )


total_scheduled_flights = len(flights)

cancelled_count = 0
delayed_count = 0
on_time_count = 0
total_passengers = 0
over_capacity_count = 0

# For the average, only "active" flights count
active_passenger_flight_count = 0

# Manual "largest passengers" search
busiest_flight = None

for flight in flights:
    if flight["cancelled"]:
        cancelled_count += 1
    elif flight["delay_minutes"] >= 1:
        delayed_count += 1
    else:
        on_time_count += 1

    # Skip 0-passenger flights when building the "active" average -
    # continue is used here because there's nothing to add
    if flight["passengers"] == 0:
        continue
    
    active_passenger_flight_count += 1
    
    total_passengers += flight["passengers"]

    if flight["passengers"] / flight["max_capacity"] > 0.8:
        over_capacity_count += 1

    if busiest_flight is None or flight["passengers"] > busiest_flight["passengers"]:
        busiest_flight = flight

average_passengers = total_passengers / active_passenger_flight_count

print("Total scheduled flights:", total_scheduled_flights)
print("Cancelled flights:", cancelled_count)
print("Delayed flights:", delayed_count)
print("On-time flights:", on_time_count)
print("Total passengers:", total_passengers)
print("Average passengers (active flights):", round(average_passengers, 2))
print(f"Busiest flight: {busiest_flight['flight_number']} - "
      f"{busiest_flight['destination']} - {busiest_flight['passengers']} passengers")
print("Flights above 80% capacity:", over_capacity_count)


searched_flight_number = input("Enter flight number: ")

found_flight = None
for flight in flights:
    if flight["flight_number"] == searched_flight_number:
        found_flight = flight
        break  # no reason to keep searching once it's found

if found_flight is not None:
    gate_display = found_flight["gate"] if found_flight["gate"] is not None else "Gate not assigned"

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
