import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        try:
            # Prompt the user to enter their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess to the generated number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
