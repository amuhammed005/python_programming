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
