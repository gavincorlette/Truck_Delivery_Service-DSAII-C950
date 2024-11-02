


import csv

with open('csv_files/addresses.csv') as csvfile1:
    csv_address = csv.reader(csvfile1, delimiter=',')

with open('csv_files/distances.csv') as csvfile2:
    csv_distance = csv.reader(csvfile2, delimiter=',')

with open('csv_files/package_file.csv') as csvfile3:
    csv_package = csv.reader(csvfile3, delimiter=',')