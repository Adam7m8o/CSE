import csv

with open("Sales") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[2] == "Fruits":
            if row[13] == 'Total Profit':
                continue
            profit = row[13]
            # print(float(profit))

    # for row in csv_reader:
    #     Thing = len(list("Sales"))
