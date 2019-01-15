# import random
import random

# variables
tries = 8
guesses = []
Win = False

# word bank
word = ("Hello", "Goodbye", "Hollow Knight", "Flex Tape", "Thatsa lotta damage", "Lilo and stich",
"Megalovania", "Undertale's Fanbase", "million", "Lion King")

# word choice
Word = random.choice(word)

# Make word list
Word = list(Word)
print(Word)

# loop
while tries > 0:
    guesses = input("choose a letter")

    tries -= 1
    if tries == 0:
        Win = False

'''
# win/lose
if Win = True:
    print("You win")

if Win = False:
    print("You lose")

# For i in range(len(Word))
'''