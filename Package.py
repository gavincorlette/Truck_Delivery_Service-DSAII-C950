
class Package:
    def __init__(self, ID, address, city, state, zip_code, delivery_deadline, weight):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight

    def __str__(self):
        return f'{self.ID}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_deadline}, {self.weight}'
