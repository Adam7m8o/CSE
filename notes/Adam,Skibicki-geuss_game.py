import random
a = (random.randint(1, 10))
loop = 0
answer = 0
while loop <= 4:
    answer = int(input("pick a number between 1 and 10"))
    if answer == a:
        print("You did it!!!!!!!")
        loop = 5
    elif answer < a:
        print("Higher")
        loop += 1
    elif answer > a:
        print("lower")
        loop += 1
    if loop == 5:
        print("you lose")