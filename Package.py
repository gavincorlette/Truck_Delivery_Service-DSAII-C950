
# Create package class
class Package:
    def __init__(self, ID, address, city, state, zip_code, delivery_deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return f'{self.ID}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_deadline}, {self.weight}, {self.status}, {self.delivery_time}'

    # Moved the logic for updating package status to this method
    def update_status(self, convert_time):
        if convert_time < self.departure_time:
            self.status = 'At Hub'
        elif self.departure_time < convert_time <= self.delivery_time:
            self.status = 'En Route'
        else:
            self.status = 'Delivered'