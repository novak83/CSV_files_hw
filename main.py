import csv

with open("list.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"{row[0]} is {row[1]} years old and {row[2]}")