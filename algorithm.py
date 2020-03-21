import time

def execute_something():
    choice = input("Choose either km/L or L/100km ")
    if choice == "km/L":
        print(consumption_1, "kilometers per liter")

    elif choice == "L/100km":
        print(consumption_2, "L/100km")
    else:
        print("Wrong input!")
    time.sleep(20)

while True:
    distance = float(input("Distance covered - "))
    fuel_initial = float(input("Amount of fuel before the start of the trip - "))
    fuel_left = float(input("Amount of fuel left - "))

    fuel_consumed = fuel_initial - fuel_left
    consumption_1 = distance / fuel_consumed
    consumption_1 = round(consumption_1, 1)
    consumption_2 = round(100 / consumption_1, 1)

    execute_something()





