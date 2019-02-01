# import random
import random

# variables
tries = 8
guesses = []
asterisk = []

# Win Condition
Win = False

# Word bank
word = ("Hello", "Goodbye", "Hollow Knight", "Flex Tape", "Thatsa lotta damage", "Lilo and stich",
"Megalovania", "Undertale's Fanbase", "million", "Lion King")

# word choice
Word = random.choice(word)

# Make word list
Word = list(Word)

# for loop / make the word asterisks
for letters_in_word in range(len(Word)):
    asterisk.append("*")

# print the thing
print(asterisk)

# loop
while tries > 0:
    guesses.append(input("choose a letter"))
    if guesses in Word:
        asterisk.[guesses]
    print(asterisk)

    tries -= 1

if tries == 0:
    Win = False

print(guesses)
print(Word)


# win/lose
if Win == True:
    print("You win")

if Win == False:
    print("You lose")