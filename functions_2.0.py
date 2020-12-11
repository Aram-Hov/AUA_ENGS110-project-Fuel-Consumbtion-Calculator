import json
import time
import Vehicle


def load_vehicle_data():
    with open("data.JSON") as f:
        data = json.load(f)
    return data


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:



    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.size = 1
            return
        newNode = Node(value)
        newNode.prev = self.head
        self.head.next = newNode
        self.head = newNode
        self.size += 1

    def printList(self):

        while self.head.prev is not None:
            print(self.head.value)
            self.head = self.head.prev
            # if self.head.next is not None :
        print(self.head.value)

    def removeLastNode(self):
        prev = self.head.prev
        self.head = prev
        self.size -= 1

    def removeNode(self, index):
        head = self.head
        size = 0
        if index < 0 or index >= self.size:
            return
        if index == (self.size - 1):
            self.removeLastNode()
            return
        if index == 0:
            while self.head.prev is not None:
                self.head = self.head.prev
            self.head.next.prev = None
            self.head = None
            self.head = head
            self.size -= 1
            return
        while (size != (self.size - index - 1)):
            size += 1
            self.head = self.head.prev
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = head
        self.size -= 1

    def addNodeAt(self, value, index):
        if index < 0 or index >= (self.size):
            return
        head = self.head
        newNode = Node(value);
        size = 0
        while (size != (self.size - index)):
            size += 1
            self.head = self.head.prev
        next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head

        newNode.next = next
        next.prev = newNode
        # print(cur.next.value)
        self.head = head
        self.size += 1
ll = LinkedList()
linkedList=LinkedList()



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



def simulate_real_time_consumption_to_List(data):
    for sample in data["trip_simulating_values"]:
        distance = 0.3
        consumption_km_per_L = distance / sample
        consumption_km_per_L = round(consumption_km_per_L, 1)
        consumption_L_per_100km = round(100 / consumption_km_per_L, 1)
        linkedList.addNode(consumption_L_per_100km)


def printConsumption():

    head=linkedList.head
    while head!=None:
        print(head.value)
        time.sleep(1)
        head=head.prev

def print_vehicle_list():

    current = ll.head
    while current != None:
        consumption_L_per_100km = calculations_for_specific_vehicles(current.value.fuel_for_03km)
        print("\n\n", current.value.brand, current.value.series, "consumes", consumption_L_per_100km, "L/100km", end="")
        current = current.prev


def add_vehicles_to_linked_list(data):
    for vehicle in data["vehicle_brands"]:
        car = Vehicle.Vehicle(vehicle["brand"], vehicle["series"], vehicle["fuel for 0.3km"])
        ll.addNode(car)




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

        current = ll.head
        while current != None:
            consumption_L_per_100km = calculations_for_specific_vehicles(current.value.fuel_for_03km)
            if lower_bound < consumption_L_per_100km < upper_bound:
                print("\n\n", current.value.brand, current.value.series, "consumes", consumption_L_per_100km, "L/100km",
                      end="")
                current = current.prev

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

        current=ll.head
        while current != None:
            if current.value.brand == brand:
                brand_found=True
                if current.value.series==series:
                    series_found=True
                    consumption_L_per_100km = calculations_for_specific_vehicles(current.value.fuel_for_03km)
                    print("\n\n", current.value.brand, current.value.series, "consumes", consumption_L_per_100km, "L/100km",
                    end="")

                    break
            current=current.prev

        if brand_found == False:
            print("the brand", brand, "was not found")

        elif series_found == False:
            print("the series", series, "not found")
        else:
            break


def execution_of_choosen_feature(story):
    data = load_vehicle_data()
    if story == "1":
        simulate_real_time_consumption_to_List(data)
        printConsumption()
    elif story == "2":
        print_vehicle_list()
    elif story == "3":
        vehicle_list_print_in_range(data)
    elif story == "4":
        vehicle_lookup()
