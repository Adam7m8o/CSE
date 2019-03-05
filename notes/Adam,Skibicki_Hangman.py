# imports
import random
import string

# variables
word = ("Hello", "Goodbye", "Hollow Knight", "Flex Tape", "Thatsa lotta damage", "Lilo and stich",
        "Megalovania", "Undertale's Fanbase", "million", "Lion King")
guesses = []
Random_Word = (random.choice(word))
underscores = []
tries = 8

for characters in Random_Word:
    underscores.append("*")
print("".join(underscores))

while tries > 0:
    print("Take a guess")
    guesses.append(input())
    if guesses == Random_Word.upper():
        current_index = underscores.index(guesses)
        underscores.pop(current_index)
        underscores.insert(current_index, string.ascii_letters)
        print("".join(underscores))
    else:
        print("That's not in the word")
        tries -= 1
print(Random_Word)
print(guesses)
