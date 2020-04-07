import json
import time
import functions

with open("data.JSON") as f:
    data = json.load(f)

story = input("Press 1 for Trip or 2 for brand/model - ")

if story == "1":
    for sample in data["trip_simulating_values"]:
        functions.calculate_1(sample)
        time.sleep(1)
    print("Trip is over, goodbye!")

elif story == "2":
    for vehicle in data["vehicle_brands"]:
        functions.calculate_2(vehicle)

