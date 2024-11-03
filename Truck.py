
# Create truck class
class Truck:
    def __init__ (self, package_list, departure_time):
        self.package_list = package_list
        self.departure_time = departure_time

    def __str__(self):
        return f'{self.package_list}, {self.departure_time}'