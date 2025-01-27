# Python Quiz Game
title = ("welcome to the python quiz game!").upper()
print(title)

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ",
             )
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Diaoxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           )

answers = ("C","D","A","A","B")
possible_options = ("A, B, C, D")
guesses = []
score = 0
question_num = 0

wrong = 0

for question in questions:
    print("------------------------")
    print(f"Q{question_num + 1}. {question}")
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter (A, B, C, D): ").upper();
        try:
            if guess not in possible_options:
                print("Invalid option")
            else:
                guesses.append(guess)
                break
        except IndexError:
            print("Please option can only be from A, B, C, and D")
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        wrong +=1
        print("INCORRECT!")
        print(f"{answers[question_num]} is the coorect answer")
    
    question_num += 1
print(f"You have answered {score} correct and {wrong} wrong")
