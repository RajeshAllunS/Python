# Import all the required modules for this program
from art import logo
import random

# Choose a random number between 1 and 100 including both
number = random.randint(1, 100)

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


# Function to return the number of attempts based on the difficulty level
def difficulty(difficulty_level):
    """ returns number of turns based on the difficulty """
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5


# Function to compare the number with the guess
def compare(guess, random_number):
    """ Compare two numbers and print high or low based on the result """
    if guess > random_number:
        print("Too high")
        # return -1
    elif guess < random_number:
        print("Too Low")


def game():
    """ Guess the random number Game """

    # Number of attempts based on the difficulty type
    count = difficulty(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

    is_guess_correct = False
    while not is_guess_correct:
        guess = int(input(f"Make a guess: "))
        if guess == number:
            print(f"You Guess it right! The number was {number}")
            is_guess_correct = True
        elif guess != number:
            compare(guess,number)
            count -= 1
        if count == 0:
            print("You've run out of guesses, you lose.")
            is_guess_correct = True
        elif count != 0 and guess != number:
            print(f"You have {count} attempts left")
            print("Guess Again")


game()
