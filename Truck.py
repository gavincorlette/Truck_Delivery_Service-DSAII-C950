
# Create truck class
class Truck:
    def __init__ (self, avg_speed, package_list, current_address, departure_time, mileage):
        self.avg_speed = avg_speed
        self.package_list = package_list
        self.current_address = current_address
        self.departure_time = departure_time
        self.mileage = mileage

    def __str__(self):
        return f'{self.avg_speed}, {self.package_list}, {self.current_address}, {self.departure_time}, {self.mileage}'

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
