
# Create truck class
class Truck:
    def __init__ (self, package_list):
        self.package_list = package_list

    def __str__(self):
        return f'{self.package_list}'