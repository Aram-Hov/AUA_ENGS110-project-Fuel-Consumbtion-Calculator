import json
import time


def load_vehicle_lists():
    with open("data.JSON") as f:
        data = json.load(f)
    return data


def choose_story():
    while True:
        story = input("Press 1 for Trip simulation \nPress 2 for brand/model search \nPress 3 to look up in specific range \n>>>")
        if story not in ('1', '2', '3',):
            print("Not an appropriate choice. Try again!")
        else:
            break

    return story


def simulation():
    data = load_vehicle_lists()
    for sample in data["trip_simulating_values"]:
        distance = 0.3
        consumption_1 = distance / sample
        consumption_1 = round(consumption_1, 1)
        consumption_2 = round(100 / consumption_1, 1)
        print(consumption_2, "L/100km")
        time.sleep(1)
    print("Trip is over, goodbye!")


def vehicle_list():
    data = load_vehicle_lists()
    for vehicle in data["vehicle_brands"]:
        distance = 0.3
        fuel_consumed = vehicle["fuel for 0.3km"]
        consumption_1 = distance / fuel_consumed
        consumption_1 = round(consumption_1, 1)
        consumption_2 = round(100 / consumption_1, 1)

        print("\n\n", vehicle["brand"], vehicle["series"], "consumes", consumption_2, "L/100km", end="")

def vehicle_list_range_search():
    while True:
        while True:
            lower_bound = input('\nEnter lowest bound you are looking for > ')
            if lower_bound.isnumeric():
                lower_bound = float(lower_bound)
                break
            else:
                print("\nYour input is not numeric, please try again!")
        while True:
            upper_bound = input('\nEnter the upper bound you are looking for > ')
            if upper_bound.isnumeric():
                upper_bound = float(lower_bound)
                break
            else:
                print("\nYour input is not numeric, please try again!")
        if lower_bound >= upper_bound:
            print("lower bound can not be greater than upper bound, please try again!")
        else:
            break


    data = load_vehicle_lists()
    for vehicle in data["vehicle_brands"]:
        distance = 0.3
        fuel_consumed = vehicle["fuel for 0.3km"]
        consumption_1 = distance / fuel_consumed
        consumption_1 = round(consumption_1, 1)
        consumption_2 = round(100 / consumption_1, 1)
        if lower_bound < consumption_2 < upper_bound :
            print("\n\n", vehicle["brand"], vehicle["series"], "consumes", consumption_2, "L/100km", end="")





def choice_of_story(story):
    if story == "1":
        simulation()
    elif story == "2":
        vehicle_list()
    elif story == "3":
        vehicle_list_range_search()

