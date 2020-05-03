import json
import time


def load_vehicle_data():
    with open("data.JSON") as f:
        data = json.load(f)
    return data




def choose_story():
    while True:
        story = input("Press 1 for Trip simulation \nPress 2 for brand/model search \nPress 3 to look up in specific "
                      "range \nPress 4 to search for a vehicle \n>>> ")
        if story not in ('1', '2', '3', '4'):
            print("Not an appropriate choice. Try again!")
        else:
            break

    return story

def calculations_for_specific_vehicles(fuel_consumed):
    distance = 0.3
    consumption_km_per_L = distance / fuel_consumed
    consumption_km_per_L = round(consumption_km_per_L, 1)
    consumption_L_per_100km = round(100 / consumption_km_per_L, 1)
    return consumption_L_per_100km



def simulate_real_time_consumption(data):
    for sample in data["trip_simulating_values"]:
        distance = 0.3
        consumption_km_per_L = distance / sample
        consumption_km_per_L = round(consumption_km_per_L, 1)
        consumption_L_per_100km = round(100 / consumption_km_per_L, 1)
        print(consumption_L_per_100km, "L/100km")
        time.sleep(1)
    print("The trip is over, have a nice day!")


def print_vehicle_list(data):
    for vehicle in data["vehicle_brands"]:
        consumption_L_per_100km = calculations_for_specific_vehicles(vehicle["fuel for 0.3km"])
        print("\n\n", vehicle["brand"], vehicle["series"], "consumes", consumption_L_per_100km, "L/100km", end="")


def vehicle_list_print_in_range(data):
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
                upper_bound = float(upper_bound)
                break

            elif float(lower_bound) >= float(upper_bound):
                print("lower bound can not be greater than upper bound, please try again!")

            else:
                print("\nYour input is not numeric or is negative, please try again!")

                break
        counter = 0
        for vehicle in data["vehicle_brands"]:
            consumption_L_per_100km = calculations_for_specific_vehicles(vehicle["fuel for 0.3km"])
            if lower_bound < consumption_L_per_100km < upper_bound :
                print("\n\n", vehicle["brand"], vehicle["series"], "consumes", consumption_L_per_100km, "L/100km", end="")
                counter += 1
        if counter == 0 :
            print("No vehicle was found in the given range, try again!")
        else:
            print("\n\nOverall", "{} matches found.".format(counter))
            break


def vehicle_lookup():

    data = load_vehicle_data()

    brand_found = False
    series_found = False

    while True:
        if (brand_found == False):
            brand = input("Insert the brand of the vehicle you are looking for > ")
            brand = brand.lower()

        series = input("Insert the model of the vehicle you are looking for > ")
        series = series.lower()

        for vehicle in data["vehicle_brands"]:

            if vehicle['brand'] == brand:
                brand_found = True
                if vehicle['series'] == series:
                    series_found = True
                    consumption_L_per_100km = calculations_for_specific_vehicles(vehicle["fuel for 0.3km"])

                    print(brand, series, "consumes", consumption_L_per_100km, "L/100km")
                    break

        if brand_found == False:
            print("the brand", brand, "was not found")

        elif series_found == False:
            print("the series", series, "not found")
        else:
            break


def execution_of_choosen_feature(story):
    data = load_vehicle_data()
    if story == "1":
        simulate_real_time_consumption(data)
    elif story == "2":
        print_vehicle_list(data)
    elif story == "3":
        vehicle_list_print_in_range(data)
    elif story == "4":
        vehicle_lookup()

