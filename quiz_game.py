# Python Quiz Game

def display_question(question_num, question, options):
    print("------------------------")
    print(f"Q{question_num}. {question}")
    for option in options:
        print(option)

def get_user_guess():
    valid_options = {"A", "B", "C", "D"}
    while True:
        guess = input("Enter (A, B, C, D): ").upper()
        if guess in valid_options:
            return guess
        print("Invalid option! Please enter A, B, C, or D.")

def calculate_score(guesses, answers):
    score = 0
    for guess, answer in zip(guesses, answers):
        if guess == answer:
            score += 1
    return score


def quiz_game():
    title = "WELCOME TO THE PYTHON QUIZ GAME!"
    print(title);

    questions = [
        "How many elements are in the periodic table?: ",
        "Which animal lays the largest eggs?: ",
        "What is the most abundant gas in Earth's atmosphere?: ",
        "How many bones are in the human body?: ",
        "Which planet in the solar system is the hottest?: ",
        "What is the capital of France?: ",
        "Who painted the Mona Lisa?: ",
        "What is the square root of 144?: ",
        "What is the largest mammal in the world?: ",
        "What is the chemical symbol for gold?: ",
    ]
    options = [
        ("A. 116", "B. 117", "C. 118", "D. 119"),
        ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
        ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
        ("A. 206", "B. 207", "C. 208", "D. 209"),
        ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
        ("A. Berlin", "B. Rome", "C. Paris", "D. Madrid"),
        ("A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"),
        ("A. 10", "B. 12", "C. 14", "D. 16"),
        ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Orca"),
        ("A. Au", "B. Ag", "C. Fe", "D. Hg"),
    ]
    answers = ["C", "D", "A", "A", "B", "C", "B", "B", "A", "A"]
    
    is_running = True
    while is_running:
        guesses = []
        for i, question in enumerate(questions, start=1):
            display_question(i, question, options[i - 1])
            guess = get_user_guess()
            guesses.append(guess)
            if guess == answers[i - 1]:
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"The correct answer is: {answers[i - 1]}")

        print("Answers: ", end=" ")
        for answer in answers:
            print(answer, end=" ")
        print()

        print("Guesses: ", end=" ")
        for guess in guesses:
            print(guess, end=" ")
        print()
        
        score = calculate_score(guesses, answers)
        percentage_score = (score / len(questions)) * 100
        print("------------------------------------------")
        print("RESULTS")
        print("------------------------------------------")
        print(f"You answered {score}/{len(questions)} questions correctly!")
        print(f"You'ved scored: {percentage_score}%")
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            is_running = False
            print("👋 Thanks for playing! See you next time! 🎮")

# Run the quiz game
quiz_game()