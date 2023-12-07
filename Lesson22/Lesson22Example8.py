#There is csv module in Python. This module simplifies work with csv files.
import csv

fileName = "file8.csv"

customers = [
    ["Solverson", 35],
    ["Jackson", 29]
    ]
with open(fileName, "w", newline="") as fileInUse:
    writer = csv.writer(fileInUse)
    writer.writerows(customers)
    
with open(fileName, "a", newline="") as fileInUse:
    customer = ["Smith", 25]
    writer = csv.writer(fileInUse)
    writer.writerow(customer)
    
with open(fileName, "r", newline="") as fileInUse:
    reader=csv.reader(fileInUse)
    for i in reader:
        print("Name: {}, Age: {}".format(i[0], i[1]))