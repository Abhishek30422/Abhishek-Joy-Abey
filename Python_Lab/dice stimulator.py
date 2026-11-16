
import random

print("===== DICE SIMULATOR =====")

while True:

    choice = input("Press Enter to roll the dice or type 'q' to quit: ")

    if choice.lower() == "q":
        print("Thanks for playing!")
        break

    dice = random.randint(1, 6)

    print("You rolled:", dice)
