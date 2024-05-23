import random


def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        number_of_attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            break


if __name__ == "__main__":
    guess_the_number()
