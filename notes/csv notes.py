import csv


def validate(num: str):
    first_num = int(num[0])
    if first_num % 1 == 1:
        return True
    return False
    second_num = int(num[1])
    if second_num % 2 == 0:

# with open("book1.csv", "r") as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = int(row[0]) +1
#         old_number = row[0]
#         print(old_number)
# if first_num % 2 == 0:
#if first_num == 4:


with open("book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")

        for row in reader:
            old_number = row[0]  # string
            if validate(old_number):
                writer.writerow(row)
        print("Okay")
