
# Create truck class
class Truck:
    def __init__ (self, package_list, address, departure_time):
        self.package_list = package_list
        self.address = address
        self.departure_time = departure_time

    def __str__(self):
        return f'{self.package_list}, {self.address}, {self.departure_time}'

    # Removes package from package_list when delivered
    def deliver_package(self, package):
        if package in self.package_list:
            self.package_list.remove(package)

    # Returns True if there are still packages in package_list
    def packages_to_deliver(self):
        if len(self.package_list) > 0:
            return True
        elif len(self.package_list) == 0:
            return False
