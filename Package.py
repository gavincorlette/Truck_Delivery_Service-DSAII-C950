from datetime import timedelta


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
        self.truck_number = None

    def __str__(self):
        return f'{self.ID}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_deadline}, {self.weight}, {self.status}, {self.delivery_time}, {self.truck_number}'

    # Moved the logic for updating package status to this method
    def update_status(self, convert_time):
        if convert_time < self.departure_time:
            self.status = 'At Hub'
        elif self.departure_time < convert_time <= self.delivery_time:
            self.status = 'En Route'
        else:
            self.status = 'Delivered'

    # Display old address for package 9 if user looks up time before 10:20
    def update_address(self, convert_time):
        if convert_time < timedelta(hours=10, minutes=20, seconds=0):
            self.address = '300 State St'
            self.zip_code = '84103'
        else:
            self.address = '410 S. State St'
            self.zip_code = '84111'