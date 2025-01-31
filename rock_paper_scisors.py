import random

print("WELCOME TO THE ROCK, PAPER, AND SCISSORS GAME! 🎮")

options = {1: "🪨  rock", 2: "📜 paper", 3: "✂ scissors"}

print(f"\nSelect one of the options to start play.")

for key, value in options.items():
    print(f"{key}: {value}")

is_running = True

while is_running:
    user_guess = input(f"\nEnter your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess not in options:
            print("❌ Invalid choice. Please select 1 (Rock), 2 (Paper), or 3 (Scissors).")
            continue

        computer_guess = random.randint(1, 3)
        # Show choices
        print(f"\n🧑 You chose: {options[user_guess]}")
        print(f"🤖 Computer chose: {options[computer_guess]}")

        
        if user_guess == computer_guess:
            print("🤝 It's a draw!")
        elif (user_guess == 1 and computer_guess == 3) or \
            (user_guess == 2 and computer_guess == 1) or \
            (user_guess == 3 and computer_guess == 2):
            print("🎉 You won!")
        else:
            print("😢 You lost!")
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            is_running = False
            print("👋 Thanks for playing! See you next time! 🎮")
    else:
        print("❌ Invalid choice. Please try again!")
