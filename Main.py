# Student Name: Gavin Corlette
# StudentID: 009934028
# WGU Data Structures and Algorithms II (C950) PA


import csv
from HashMap import ChainingHashTable
from Package import Package
from Truck import Truck
import datetime

# Create hash table
hash_map = ChainingHashTable()
# Array to hold distances
distance_list = []

with open('csv_files/addresses.csv') as csvfile1:
    csv_address = csv.reader(csvfile1, delimiter=',')
    csv_address = list(csv_address)

# Read distances.csv and insert into distance_list
with open('csv_files/distances.csv') as csvfile2:
    csv_distance = csv.reader(csvfile2, delimiter=',')
    for row in csv_distance:
        distance_list.append(row)
        hash_map.insert(row[0], row[1])

with open('csv_files/package_file.csv') as csvfile3:
    csv_package = csv.reader(csvfile3, delimiter=',')
    for row in csv_package:
        ID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        delivery_deadline = row[5]
        weight = row[6]

        # Package object
        p = Package(ID, address, city, state, zip_code, delivery_deadline, weight)

        #Insert package into hash table
        hash_map.insert(ID, p)

# Method to find index of passed in address
def find_address_index(file_name, target_address):
    with open(file_name, mode = 'r') as csvfile:
        csv_address = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_address):
            if target_address in row:
                return index
    return -1
## example usage of above def
#index = find_address_index('csv_files/addresses.csv', '4001 South 700 East')
#print(index)

# method to find distance between 2 values
def distance_between(x_val, y_val):
    distance = csv_distance[x_val][y_val]
    if distance == '':
        distance = csv_distance[y_val][x_val]
    return float(distance)


# Load all 3 trucks
truck1 = Truck([15, 14, 19, 16, 13, 20, 1, 13, 15, 29, 30, 31, 34, 37, 40, 2], "4001 South 700 East", datetime.timedelta(hours = 8, minutes = 0)) # leave at 8:00

truck2 = Truck([3, 18, 36, 38, 6, 25, 28, 32, 4, 5, 7, 8, 10, 11, 12, 17], "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5)) # leave at 9:05

truck3 = Truck([9, 19, 21, 22, 23, 24, 26, 27, 33, 35, 39], "4001 South 700 East", datetime.timedelta(hours = 10, minutes = 20)) # leave at/after 10:20