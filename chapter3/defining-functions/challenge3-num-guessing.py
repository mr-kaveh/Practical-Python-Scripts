import random

# Define a function to play the number-guessing game
def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Can you guess it?")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the secret number, which was {secret_number}!")
            break

        attempts += 1

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

# Call the function to play the game
play_guessing_game()
