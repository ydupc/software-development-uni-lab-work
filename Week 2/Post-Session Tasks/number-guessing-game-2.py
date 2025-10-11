import random

def play_single_round():
    """Play one round of the number guessing game."""
    random_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    guess = None

    print("\n🎯 New Round! Guess the number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess → "))
            if guess < 1 or guess > 100:
                print("❗ Please guess a number within 1–100.\n")
                continue

            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {random_number}.")
                print(f"You guessed it in {attempts} attempts.\n")
                return attempts  # Return score (number of attempts used)

            remaining = max_attempts - attempts
            print(f"🔢 Attempts remaining: {remaining}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    print(f"😢 You've used all {max_attempts} attempts. The correct number was {random_number}.\n")
    return max_attempts  # If failed, max attempts count as score


def play_game():
    """Play multiple rounds of the guessing game."""
    total_rounds = 3
    total_score = 0

    print("🎮 Welcome to the Multi-Round Number Guessing Game!")
    print(f"You’ll play {total_rounds} rounds in total.\n")

    for round_number in range(1, total_rounds + 1):
        print(f"==============================")
        print(f"🏁 Starting Round {round_number}")
        print(f"==============================")
        score = play_single_round()
        total_score += score
        print(f"Round {round_number} complete! Attempts this round: {score}")
        print(f"Your running total: {total_score}\n")

    print("=====================================")
    print("🏆 Game Over – Final Results 🏆")
    print(f"Total attempts across all rounds: {total_score}")
    avg_attempts = total_score / total_rounds
    print(f"Average attempts per round: {avg_attempts:.2f}")

    if avg_attempts <= 7:
        print("🌟 Excellent guessing skills!")
    elif avg_attempts <= 9:
        print("👍 Good job!")
    else:
        print("💡 Better luck next time!")

    print("=====================================\n")


if __name__ == "__main__":
    play_game()
