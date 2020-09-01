class PowerBank:
    def __init__(self, colour, num_of_ports, battery_capacity):
        self.battery_capacity = battery_capacity
        self.num_of_ports = num_of_ports
        self.colour = colour

    def all_attributes(self):
        return self.all_attributes()
    def bat_capacity(self):
        return int(self.battery_capacity())

    def colour(self):
        return self.colour()

    def printer(self):
        print(self.battery_capacity())


pow_bank1 = PowerBank("black", 4, 6000)
pow_bank2 = PowerBank("white", 2, 2500)
pow_bank3 = PowerBank('red,', 5, 20000)
print(PowerBank.battery_capacity(pow_bank1))

