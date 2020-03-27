import time
import json
with open("data.JSON") as f:
    data = json.load(f)


measurment_system = input("Press 1 for km/L or 2 for L/100km - ")

def print_result():
    if measurment_system == "1":
        print(consumption_1, "kilometers per liter")

    elif measurment_system == "2":
        print(consumption_2, "L/100km")
    else:
        print("Wrong input!")

    time.sleep(3)

fuel_trip = [0.025, 0.03, 0.015, 0.0416, 0.0263, 0.0356, 0.0852, 0.0541, 0.0476, 0.0769]


choice = input("Press 1 for Trip or 2 for brand/model")
if choice == "2":
    for vehicle in data["vehicle_brands"]:
        distance = 0.3
        fuel_consumed = vehicle["fuel for 0.3km"]
        consumption_1 = distance / fuel_consumed
        consumption_1 = round(consumption_1, 1)
        consumption_2 = round(100 / consumption_1, 1)
        print_result()
elif choice == "1":
    distance = 0.3

    for sample in fuel_trip:

        consumption_1 = distance / sample
        consumption_1 = round(consumption_1, 1)
        consumption_2 = round(100 / consumption_1, 1)


