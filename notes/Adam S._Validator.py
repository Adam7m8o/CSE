import csv

# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers - Done
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10


def check_how_long(num: str):
    if len(num) == 16:
        return True
    return False


def remove(num: str):
    if len(num) == 16:
        print(num[15])


def reverse(num: str):
    print(num)
    print(num[::-1])


def multiply_odd(num: str):

