import random

def number_guesser():
    print("Welcome to Number Guesser Game!")

    # user-defined range
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))

    number = random.randint(lower, upper)
    attempts = 0

    print(f"\nI have selected a number between {lower} and {upper}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number!")

number_guesser()