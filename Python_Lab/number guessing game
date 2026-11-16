
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("===== NUMBER GUESSING GAME =====")
print("I have selected a number between 1 and 100.")

guess = 0
attempts = 0

while guess != secret_number:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Congratulations! You guessed the correct number.")
        print("Number of attempts:", attempts)

print("===== GAME OVER =====")
