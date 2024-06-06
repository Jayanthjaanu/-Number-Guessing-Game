import random


def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly. Good luck!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Hint: The number is higher than your guess.")
        elif guess > number_to_guess:
            print("Hint: The number is lower than your guess.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts!")
            break
    else:
        print(
            f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!")


if __name__ == "__main__":
    guessing_game()
