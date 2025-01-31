import random

lowest_number = 1
highest_number = 100
guesses = 0
guess_limit = 10
is_running = True

print("🎉 Welcome to the Number Guessing Game! 🎉")
print(f"I've picked a number between {lowest_number} and {highest_number}. Can you guess it?")
answer = random.randint(lowest_number, highest_number)

while is_running:
    guess = input(f"\nEnter your guess ({lowest_number}-{highest_number}): ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        guess_limit -= 1

        if guess < lowest_number or guess > highest_number:
            print(f"⚠️ Please enter a number between {lowest_number} and {highest_number}. Try again!")
        elif guess > answer:
            print(f"📉 Too high! You have {guess_limit} {'guesses' if guess_limit != 1 else 'guess'} left. Keep going!")
        elif guess < answer:
            print(f"📈 Too low! You have {guess_limit} {'guesses' if guess_limit != 1 else 'guess'} left. Keep trying!")
        else:
            print(f"🎉 Congratulations! You guessed it right! The number was {answer}. It took you {guesses} {'trial' if guesses == 1 else 'tries' }. 🎉")
            break

        if guess_limit == 0:
            print(f"😢 Oh no! You've run out of guesses. The correct number was {answer}. Better luck next time!")
            break
    else:
        print("❌ Invalid input! Please enter a valid number.")

print("Thanks for playing! 🎮")
