# import random
import random

# variables
tries = 8
guess = []
asterisk = []
please = []

# Win Condition
Win = False

# Word bank
word = ("Hello", "Goodbye", "Hollow Knight", "Flex Tape", "Thatsa lotta damage", "Lilo and stich",
"Megalovania", "Undertale's Fanbase", "million", "Lion King")

# word choice
Word = random.choice(word)

# Make word list
Word = (list(Word))

# for loop / make the word asterisks
for letters_in_word in range(len(Word)):
    asterisk.append("*")

# print the thing
print(asterisk)

# loop
while tries > 0:
    guess.append(input("choose a letter"))
    if guess in Word:
        asterisk = asterisk(Word, asterisk, guess)
    print(asterisk)
else:
    tries -= 1

if tries == 0:
    Win = False

print(guess)
print(str(Word))


# win/lose
if Win == True:
    print("You win")
else:
    print("You lose")