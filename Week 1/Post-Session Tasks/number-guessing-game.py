import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have a maximum of 10 tries to guess it correctly.\n")

    number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1–100): "))
            if guess < 1 or guess > 100:
                print("❗ Please guess a number within 1–100.")
                continue

            attempts += 1

            if guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.\n")
    else:
        print(f"😢 You've used all {max_attempts} attempts. The correct number was {number}.")

if __name__ == "__main__":
    number_guessing_game()
