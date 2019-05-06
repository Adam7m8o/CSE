import csv


def first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False


def second_num_even(num: str):
    second_num = int(num[1])
    if second_num % 2 == 0:
        return True
    return False


def validate(num: str):
    if first_num_odd(num) and second_num_even(num):
        return True
    return False

# 41895


def reverse(num: str):
    print(num)
    print(num[::-1])


reverse("4639198752831360")


#     first_num = int(num[0])
#     if first_num % 1 == 1:
#         return True
#     return False
#     second_num = int(num[1])
#     if second_num % 2 == 0:
#         return True
#     return False

# with open("book1.csv", "r") as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = int(row[0]) +1
#         old_number = row[0]
#         print(old_number)
# if first_num % 2 == 0:
# if first_num == 4:


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
