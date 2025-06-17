import random
import time

# Step 1: Define the possible symbols (use emojis or strings)
symbols = ["🍒", "🔔", "🍋", "⭐", "7️⃣", "💎"]

def spin_reel():
    """Generates a 3x3 grid of random symbols"""
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

def display_grid(grid):
    """Nicely prints the 3x3 grid"""
    for row in grid:
        print(" | ".join(row))
    print()

def check_win(grid):
    """Check if all symbols in the middle row match"""
    middle_row = grid[1]
    return middle_row.count(middle_row[0]) == 3  # All same

def main():
    print("🎰 Welcome to the 3x3 Slot Machine Game! 🎰")
    while True:
        input("Press Enter to spin...")
        
        grid = spin_reel()

        print("\nSpinning...")
        time.sleep(1)

        display_grid(grid)

        if check_win(grid):
            print("🎉 You WIN! 🎉\n")
        else:
            print("❌ You lose. Try again!\n")

        # Ask to play again
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
