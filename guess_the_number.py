

import random
import art

# random number generator from 1 to 100
def random_number():
    number = random.randint(1, 100)
    return number

# Initial game sequence
def guess_the_number():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        easy_mode(difficulty)
    elif difficulty == "hard":
        hard_mode(difficulty)
    else:
        print("That's not a valid option.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Plays games as EASY
def easy_mode(difficulty):
    number = random_number()
    attempts = 10
    while difficulty =='easy' and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        make_a_guess = int(input("Make a guess: "))
        if make_a_guess > number:
            print("Too high.")
            print("Guess again.")
        if make_a_guess < number:
            print("Too low.")
            print("Guess again.")
        if make_a_guess == number:
            print(f"You got it! The answer was {number}.")
            play_again()
        attempts -= 1
    else:
        print("You've run out of guesses. Game Over!")

# Plays games as HARD
def hard_mode(difficulty):
    number = random_number()
    attempts = 5
    while difficulty =='hard' and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        make_a_guess = int(input("Make a guess: "))
        if make_a_guess > number:
            print("Too high.")
            print("Guess again.")
        if make_a_guess < number:
            print("Too low.")
            print("Guess again.")
        if make_a_guess == number:
            print(f"You got it! The answer was {number}.")
            play_again()
        attempts -= 1
    else:
        print("You've run out of guesses. Game Over!")
        play_again()

# Asks to play again after game end state.
def play_again():
    play_again = input("Would you like to play again? Type 'yes' or 'no': ")
    if play_again == "yes":
        print("\n" * 20)
        guess_the_number()
    else:
        print("Thanks for playing!")

guess_the_number()