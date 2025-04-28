# # import random
# # # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# # #  ● ┌ ─ ┐ │ └ ┘

# # # "┌─────────┐"
# # # "│         │"
# # # "│         │"
# # # "│         │"
# # # "└─────────┘"


# import random

# # Dice representations using ASCII art
# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘"),
# }

# # Function to print the dice art
# def print_dice(number):
#     for line in dice_art[number]:
#         print(line)

# # Function to roll a dice
# def roll_dice():
#     return random.randint(1, 6)

# # Function to handle a player's turn
# def player_turn(player_name, player_score):
#     consecutive_sixes = 0  # Track consecutive 6s

#     while True:
#         input(f"\n{player_name}, press Enter to roll the dice... 🎲")
#         roll = roll_dice()
#         print(f"\n{player_name} rolled a {roll}!\n")
#         print_dice(roll)

#         if roll == 6:
#             consecutive_sixes += 1
#             player_score.append(roll)  # Add the 6 to the score

#             if consecutive_sixes == 3:  # If player rolls 6 three times in a row, switch turn
#                 print(f"\n⚠ {player_name} rolled three 6s in a row! Their turn ends.\n")
#                 return sum(player_score)
#             else:
#                 print(f"🎉 {player_name} rolled a 6! They get another chance! 🎲")
#                 continue  # Give them another roll

#         else:
#             consecutive_sixes = 0  # Reset the streak if it's not a 6
#             player_score.append(roll)
#             return sum(player_score)

# # Function to handle replaying the game
# def play_again():
#     while True:
#         choice = input("Do you want to play again? (y/n): ").strip().lower()
#         if choice == "y":
#             return True
#         elif choice == "n":
#             print("👋 Thanks for playing! See you next time! 🎮")
#             return False
#         else:
#             print("❌ Invalid input! Please enter 'y' or 'n'.")

# # Main game loop
# while True:
#     # Game Setup
#     player1_score = []
#     player2_score = []
#     target_score = 13

#     print("\n🎲 Welcome to the Play & Pass Dice Game! 🎲\n")
#     print("First player to reach 13 points wins!\n")

#     while True:
#         # Player 1's Turn
#         print("\n🧑 Player 1's Turn:")
#         total_p1 = player_turn("Player 1", player1_score)
#         print(f"Player 1's Total Score: {total_p1}")

#         if total_p1 >= target_score:
#             print("\n🎉 Player 1 wins! 🎉")
#             break

#         # Player 2's Turn
#         print("\n🤖 Player 2's Turn:")
#         total_p2 = player_turn("Player 2", player2_score)
#         print(f"Player 2's Total Score: {total_p2}")

#         if total_p2 >= target_score:
#             print("\n🎉 Player 2 wins! 🎉")
#             break

#     # Ask if they want to play again
#     if not play_again():
#         break  # Exit the game if they choose 'n'



import random
import time

# 🎲 Dice Art Representation
DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

# 🎲 Function to Print Dice Art
def print_dice(number):
    for line in DICE_ART[number]:
        print(line)

# 🎲 Dice Rolling Function
def roll_dice():
    return random.randint(1, 6)

# 🎮 Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.consecutive_sixes = 0  # Track consecutive sixes

    def roll(self):
        """Rolls the dice and updates the score accordingly."""
        roll = roll_dice()
        print(f"\n🎲 {self.name} rolled a {roll}!")
        print_dice(roll)

        if roll == 6:
            self.consecutive_sixes += 1
            if self.consecutive_sixes == 3:  # Switch turn if 3 sixes in a row
                print(f"⚠ {self.name} rolled three 6s in a row! Turn skipped.\n")
                self.consecutive_sixes = 0  # Reset streak
                return 0  # No score added
        else:
            self.consecutive_sixes = 0  # Reset streak if not a 6

        return roll

# 🎮 Play & Pass Dice Game Class
class DiceGame:
    TARGET_SCORE = 13  # Winning Score

    def __init__(self):
        print("\n🎲 Welcome to the Play & Pass Dice Game! 🎲")
        print(f"🎯 First to reach {self.TARGET_SCORE} points wins!\n")
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def play_round(self, player):
        """Handles a player's turn."""
        while True:
            input(f"\n{player.name}, press Enter to roll the dice... 🎲")
            roll = player.roll()
            player.score += roll
            print(f"💯 {player.name}'s Total Score: {player.score}\n")

            if player.score >= self.TARGET_SCORE:
                print(f"\n🏆 {player.name} wins with {player.score} points! 🎉")
                return True

            if roll == 6:
                print(f"🎉 {player.name} rolled a 6! Rolling again...\n")
                time.sleep(1)  # Pause for better UX
                continue  # Get another turn if they rolled a 6
            else:
                break  # End turn if not a 6

        return False

    def start_game(self):
        """Starts the game loop."""
        while True:
            if self.play_round(self.player1): break  # Player 1's turn
            if self.play_round(self.player2): break  # Player 2's turn

        self.restart_game()

    def restart_game(self):
        """Asks if players want to play again."""
        while True:
            choice = input("\n🔄 Do you want to play again? (y/n): ").strip().lower()
            if choice == 'y':
                print("\n🎮 Restarting the game...\n")
                self.__init__()  # Reset players & scores
                self.start_game()
            elif choice == 'n':
                print("\n👋 Thanks for playing! See you next time! 🎲")
                exit()
            else:
                print("❌ Invalid input! Please enter 'y' or 'n'.")

# 🚀 Start the Game
if __name__ == "__main__":
    game = DiceGame()
    game.start_game()
