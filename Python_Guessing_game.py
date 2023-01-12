import random

# Generate a random number to guess
number_to_guess = random.randint(1, 100)

# Welcome the player
print("Welcome to the guessing game!")

# Get the player's first guess
guess = int(input("Take a guess: "))

# Loop until the player gets the correct number
while guess != number_to_guess:
    if guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Take a guess: "))

# The player guessed the number
print("Congratulations! You got it.")
