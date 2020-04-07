import json
variable = input("Press 1 for km/L or 2 for L/100km - ")

def calculate_1(sample):
    distance = 0.3
    consumption_1 = distance / sample
    consumption_1 = round(consumption_1, 1)
    consumption_2 = round(100 / consumption_1, 1)
    if variable == "1":
         print(consumption_1, "km/L")

    elif variable == "2":
        print(consumption_2, "L/100km")





def calculate_2(vehicle):
    distance = 0.3
    fuel_consumed = vehicle["fuel for 0.3km"]
    consumption_1 = distance / fuel_consumed
    consumption_1 = round(consumption_1, 1)
    consumption_2 = round(100 / consumption_1, 1)
    if variable == "1":
        print(vehicle["brand"], vehicle["series"], "consumes", consumption_1, "km/L")
    elif variable == "2":
        print("\n\n", vehicle["brand"], vehicle["series"], "consumes", consumption_2, "L/100km", end="")







