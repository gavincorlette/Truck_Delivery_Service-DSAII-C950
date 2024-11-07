# Student Name: Gavin Corlette
# StudentID: 009934028
# WGU Data Structures and Algorithms II (C950) PA
import csv
from HashMap import ChainingHashTable
from Package import Package
from Truck import Truck
from datetime import timedelta

# Create hash table
hash_map = ChainingHashTable()
# Hold distances
distance_list = []
# Hold addresses
address_list = []

# Opens addresses.csv and creates a list
with open('csv_files/addresses.csv') as csvfile1:
    csv_address = csv.reader(csvfile1, delimiter=',')
    for row in csv_address:
        address_list.append(row[1])

# Read distances.csv and insert into distance_list
with open('csv_files/distances.csv') as csvfile2:
    csv_distance = csv.reader(csvfile2, delimiter=',')
    for row in csv_distance:
        distance_list.append(row)
        hash_map.insert(row[0], row[1])

# Opens and loads package_file
with open('csv_files/package_file.csv') as csvfile3:
    csv_package = csv.reader(csvfile3, delimiter=',')
    next(csv_package)
    for row in csv_package:
        ID = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = int(row[4])
        delivery_deadline = row[5]
        weight = row[6]

        # Package object
        p = Package(ID, address, city, state, zip_code, delivery_deadline, weight)

        #Insert package into hash table
        hash_map.insert(ID, p)

#print(hash_map.search(1))

# Method to find index of passed in address
def find_address_index(file_name, target_address):
    with open(file_name, mode = 'r') as csvfile:
        csv_address2 = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_address2):
            if target_address in row:
                return index
    return -1
## example usage of above def
#index = find_address_index('csv_files/addresses.csv', '4001 South 700 East')
#print(index)

# method to find distance between 2 values
def distance_between(x_val, y_val):
    distance = distance_list[x_val][y_val]
    if distance == '':
        distance = distance_list[y_val][x_val]
    return float(distance)

# Load all 3 trucks
truck1 = Truck(18, [15, 14, 19, 16, 13, 20, 1, 13, 15, 29, 30, 31, 34, 37, 40, 2], '4001 South 700 East', timedelta(hours = 8, minutes = 0), 'At Hub', 0.0) # leave at 8:00

truck2 = Truck(18, [3, 18, 36, 38, 6, 25, 28, 32, 4, 5, 7, 8, 10, 11, 12, 17], '4001 South 700 East', timedelta(hours = 9, minutes = 5), 'At Hub', 0.0) # leave at 9:05

truck3 = Truck(18, [9, 19, 21, 22, 23, 24, 26, 27, 33, 35, 39], '4001 South 700 East', timedelta(hours = 10, minutes = 20), 'At Hub', 0.0) # leave at/after 10:20

# Method to find the shortest distance between two addresses
def min_distance_from(current_address, remaining_addresses):
    # Instantiate min_distance and next_address
    min_distance = float('inf')
    next_address = None

    # Loop to compare all addresses in list
    for package_id in remaining_addresses:
        # Searches hash map to map ID to package info
        package_info = hash_map.search(package_id)
        # Assigns only address portion of package info to package_address
        package_address = package_info.address

        current_index = find_address_index('csv_files/addresses.csv', current_address)
        package_index = find_address_index('csv_files/addresses.csv', package_address)

        # Call distance_between method to compare distances
        distance = distance_between(current_index, package_index)

        # Check if shortest distance is found
        if distance < min_distance:
            min_distance = distance
            next_address = package_address

    return next_address

#best_distance = min_distance_from(truck1.current_address, truck1.package_list)
#print(best_distance)
'''package = hash_map.search(3)
address = package.address
print(address)'''

## Example use of distance_between function; may need to alter as I develop algorithm
#between = distance_between(find_address_index('csv_files/addresses.csv', '195 W Oakland Ave'), find_address_index('csv_files/addresses.csv', '4580 S 2300 E'))
#print(between)

def deliver_packages(truck):

    current_time = truck.departure_time
    current_address = truck.current_address

    while truck.packages_to_deliver():
        next_package = min_distance_from(current_address, truck.package_list)

        package_id = None
        for pkg_id in truck.package_list:
            if hash_map.search(pkg_id).address == next_package:
                package_id = pkg_id
                break

        current_index = find_address_index('csv_files/addresses.csv', current_address)
        package_index = find_address_index('csv_files/addresses.csv', next_package)
        distance = distance_between(current_index, package_index)

        time_to_deliver = timedelta(hours = distance / truck.avg_speed)
        current_time += time_to_deliver

        truck.mileage += distance

        package = hash_map.search(package_id)
        package.status = "Delivered"
        package.delivery_time = current_time

        truck.deliver_package(package_id)

        current_address = next_package

    print(f"Total mileage for this truck: {truck.mileage} miles")
    return current_time

# Begin delivery of trucks 1 and 2
truck1_current_time = deliver_packages(truck1)
truck2_current_time = deliver_packages(truck2)
# Was gonna create a constraint here to make sure at least one of the trucks finished delivering before truck 3 can depart
# but I already have its departure time set to 10:20 and truck1 finished at 9:42, so all is good there
truck3_current_time = deliver_packages(truck3)
#print(truck1_current_time, truck2_current_time, truck3_current_time)

total_miles_travelled = truck1.mileage + truck2.mileage + truck3.mileage
print(total_miles_travelled)