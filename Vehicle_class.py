class Vehicle:

    def __init__(self, brand, series, fuel_for_03km):
        self.brand = brand
        self.series = series
        self.fuel_for_03km = fuel_for_03km

    def print_info(self):
        print(self.brand, self.series, self.fuel_for_03km)
