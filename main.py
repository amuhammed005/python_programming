import random

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print();

# fruits = ["apple", "apple", "apple", "orange", "banana", "coconut"]

# fruits[0] = "pineapple"

# for fruit in fruits:
#     print(fruit)
# print(help(fruits))

# fruits.append("pineapple")
# fruits.remove("apple")
# print(fruits.count("apple"))
# fruits.sort();
# fruits.insert(0, "mango")
# fruits.reverse()
# fruits.clear()
# fruits.remove("apple")


# print(fruits)
# print()


# remove2 = 1
# while remove2 <= len(fruits):
#     fruits.remove("apple")
#     if not "apple" in fruits:
#         break
#     remove2 += 1
#     print(fruits)
#     print()
    
# print(fruits)

# num_pad = ((1, 2, 3),
#            (4, 5, 6), 
#            (7, 8, 9), 
#            ("*", 0, "#")
#            )
# # print(num_pad)
# for row in num_pad:
#     # print(row, end=" ")
#     for num in row:
#         print(num, end=" ")
#     print()

# fruits = ["mango", "orange", "apple"]
# meats =  ["chicken", "goat", "cow"]
# vege =   ["salad", "chacha", "beans"]

# foods = [fruits, meats, vege]
# # print(foods)
# for food in foods:
#     for col in food:
#         print(col, end=" ")
#     print()


# PYTHON DICTIONARY
# capitals = {
#     "USA": "Washinton DC",
#     "China": "Berjing",
#     "Ghana": "Accra"
# }

# print(capitals)
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# capitals.update({"Burkina": "Tenkudogu"})
# capitals.pop("Burkina")
# capitals.update({"Burkina": "Ougadugu"})
# capitals.popitem()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

# for key, value in zip(capitals.keys(), capitals.values()):
#     print(f"{key}: {value}")
# print(capitals)
# print(keys)
# print()

# print(capitals.items())
# for key, value in capitals.items():
#     print(f"{key}: {value}")

# import random
# print(help(random))
# number = random.randint(1, 100)

# print(number)




















# import React, { useState } from "react";
# import { Card, CardContent } from "@/components/ui/card";
# import { Button } from "@/components/ui/button";

# const questions = [
#   {
#     question: "How many elements are in the periodic table?",
#     options: ["116", "117", "118", "119"],
#     answer: "118",
#   },
#   {
#     question: "Which animal lays the largest eggs?",
#     options: ["Whale", "Crocodile", "Elephant", "Ostrich"],
#     answer: "Ostrich",
#   },
#   {
#     question: "What is the most abundant gas in Earth's atmosphere?",
#     options: ["Nitrogen", "Oxygen", "Carbon-Dioxide", "Hydrogen"],
#     answer: "Nitrogen",
#   },
#   {
#     question: "How many bones are in the human body?",
#     options: ["206", "207", "208", "209"],
#     answer: "206",
#   },
#   {
#     question: "Which planet in the solar system is the hottest?",
#     options: ["Mercury", "Venus", "Earth", "Mars"],
#     answer: "Venus",
#   },
#   {
#     question: "What is the capital of France?",
#     options: ["Paris", "Rome", "Berlin", "Madrid"],
#     answer: "Paris",
#   },
#   {
#     question: "What is the largest ocean on Earth?",
#     options: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
#     answer: "Pacific Ocean",
#   },
#   {
#     question: "Which country has the highest population?",
#     options: ["India", "China", "USA", "Russia"],
#     answer: "China",
#   },
#   {
#     question: "Who wrote 'Hamlet'?",
#     options: ["Charles Dickens", "William Shakespeare", "Mark Twain", "J.K. Rowling"],
#     answer: "William Shakespeare",
#   },
#   {
#     question: "What is the square root of 64?",
#     options: ["6", "7", "8", "9"],
#     answer: "8",
#   },
# ];

# const QuizApp = () => {
#   const [currentQuestion, setCurrentQuestion] = useState(0);
#   const [score, setScore] = useState(0);
#   const [selectedOption, setSelectedOption] = useState(null);
#   const [showResult, setShowResult] = useState(false);

#   const handleOptionSelect = (option) => {
#     setSelectedOption(option);
#   };

#   const handleNextQuestion = () => {
#     if (selectedOption === questions[currentQuestion].answer) {
#       setScore(score + 1);
#     }
#     setSelectedOption(null);
#     if (currentQuestion < questions.length - 1) {
#       setCurrentQuestion(currentQuestion + 1);
#     } else {
#       setShowResult(true);
#     }
#   };

#   const handleRestart = () => {
#     setCurrentQuestion(0);
#     setScore(0);
#     setSelectedOption(null);
#     setShowResult(false);
#   };

#   return (
#     <div className="flex flex-col items-center p-6">
#       <h1 className="text-3xl font-bold mb-6">React Quiz Game</h1>
#       {showResult ? (
#         <Card className="max-w-md w-full">
#           <CardContent className="text-center">
#             <h2 className="text-2xl font-semibold">Quiz Completed!</h2>
#             <p className="mt-4 text-lg">Your score is {score} out of {questions.length}.</p>
#             <Button className="mt-6" onClick={handleRestart}>
#               Restart Quiz
#             </Button>
#           </CardContent>
#         </Card>
#       ) : (
#         <Card className="max-w-md w-full">
#           <CardContent>
#             <h2 className="text-lg font-medium mb-4">
#               Question {currentQuestion + 1}/{questions.length}
#             </h2>
#             <p className="text-xl mb-6">{questions[currentQuestion].question}</p>
#             <div className="space-y-3">
#               {questions[currentQuestion].options.map((option, index) => (
#                 <Button
#                   key={index}
#                   variant={selectedOption === option ? "solid" : "outline"}
#                   onClick={() => handleOptionSelect(option)}
#                   className="w-full"
#                 >
#                   {option}
#                 </Button>
#               ))}
#             </div>
#             <Button
#               className="mt-6 w-full"
#               onClick={handleNextQuestion}
#               disabled={!selectedOption}
#             >
#               {currentQuestion === questions.length - 1 ? "Finish" : "Next"}
#             </Button>
#           </CardContent>
#         </Card>
#       )}
#     </div>
#   );
# };

# export default QuizApp;


# Format specifier
# price1 = 3450.897
# price2 = -123809.8
# price3 = 6020.53

# print(f'Price 1: {price1:}')
# print(f'Price 2: {price2:}')
# print(f'Price 3: {price3:}')

# countdown timer program

# import time

# num = int(input("Enter your time: "))

# for x in range(num, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f'{hours:02}:{minutes:02}:{seconds:02}')
#     time.sleep(1)

# print("Time Up!")

# questions = ("1.What is my name?", 
#              "2.Where do I come from?", 
#              "3.Which school do I attend currently?")

# options = (("A. Adam", "B. Yakubu", "C. Rahma"),
#            ("A. Bolga", "B. Bawku", "C. Kumasi"),
#            ("A. Tech", "B. Winneba", "C. Legon"))

# answers = ("A", "B", "C")

# guesses = []

# score = 0

# question_num = 0


# def valid_guess():
#     while True:
#         valid_options = {"A", "B", "C"}
#         guess = input("Enter (A, B, C) or q to quit: ").upper()
#         if guess in valid_options:
#             return guess
#         print("❌ Incorrect option.")



# menu = {
#     "banku": 3.5,
#     "rice": 5,
#     "coco": 2,
#     "gobe": 2.5
# }

# cart = []

# total = 0

# print("------- Menu -------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value}")

# while True:
#     food = input("Select food to buy. (q to quit): ").lower()

#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#     else:
#         print("❌Food not listed in menu")

# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
# print()
# print(f'Your total is: ${total:.2f}')



# Rock paper scissors game

# print("---------- Welcome to python rock paper scissors game ----------")

# options = ("rock", "paper","scissors")

# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ").lower()

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if computer == player:
#         print("It's a tie")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")


#     play_again = input("Play again? y or n: ").strip().lower()
#     if not play_again == "y":
#         running = False

# print("Thanks for playing!")


# options = {1:"rock", 
#            2:"paper", 
#            3:"scissors"}

# for key, value in options.items():
#     print(f'{key}:{value}')

# converted_options = tuple(options.values())
# print('Converted_options: ',converted_options)

# # print(computer)

# playing = True
# while playing:
#     player = None
#     computer = random.choice(converted_options)

#     while player not in converted_options:
#         player = input("Please type Rock, Paper or Scissors: ").strip().lower()
#         if player not in converted_options:
#             print("❌ Invalid choice. Try again")    

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if computer == player:
#         print("It's a tie")
#     elif ((player == "rock" and computer == "scissors") or
#         (player == "paper" and computer == "rock") or
#         (player == "scissors" and computer == "paper")):
#         print("You win! 🎉")
#     else:
#         print("You lose! 🤦")
    
#     if input("Continue playing? type 'y' for yes or 'q' to Quit: ").strip().lower() != "y":
#         playing = False

# print("Thanks for playing! 😊")

# from typing import Tuple

# OPTIONS = ("rock", "paper", "scissors")

# def display_options() -> None:
#     print("\nChoices: ")
#     for idx, option in enumerate(OPTIONS, start=1):
#         print(f"{idx}: {option.capitalize()}")
#     print()

# # display_options()

# def get_player_choice() -> str:
#     while True:
#         choice = input("Type 'rock', 'paper', or 'scissors': ").strip().lower()
#         if choice in OPTIONS:
#             return choice
#         print("❌ Invalid choice. Try again\n")

# # get_player_choice()

# def get_computer_choice() -> str:
#     return random.choice(OPTIONS)

# # get_computer_choice()

# def get_winner(player: str, computer: str) -> str:
#     if(player == computer):
#         return "It's a tie!\n"
#     wins = {
#         "rock": "scissors",
#         "paper": "rock",
#         "scissors": "paper"
#     }
#     if wins[player] == computer:
#         return "You win! 🎉"
#     return "You lose!😭"
#     # if computer == player:
#     #     print("It's a tie")
#     # elif ((player == "rock" and computer == "scissors") or
#     #     (player == "paper" and computer == "rock") or
#     #     (player == "scissors" and computer == "paper")):
#     #     print("You win! 🎉")
#     # else:
#     #     print("You lose! 🤦")

# def play_round() -> None:
#     player = get_player_choice()
#     computer = get_computer_choice()

#     print(f'Player: {player}')
#     print(f'Computer: {computer.capitalize()}')

#     result = get_winner(player, computer)
#     print(f"Result: {result}")

# # play_round()

# def play_game() -> None:
#     print("\nWelcome to rock, paper, scissors game.")
#     display_options()

#     while True:
#         play_round()

#         continue_playing = input("Do you want to continue playing? Type 'y' for Yes or 'q' to Quit: ").strip().lower()
#         if continue_playing != 'y':
#             break
#     print("Thank you for playing!")

# if __name__ == "__main__":
#     play_game()


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

# for key, value in DICE_ART.items():
#     print(key)
#     for art in value:
#         print(art)

def display_art(number):
    for art in DICE_ART.get(number):
        print(art)

def roll_dice():
    return random.randint(1, 6)

# def opponent():
#     option = input("Select a player 1:Computer \n 2.Friend")

def player_turn(player_name, player_score):
    