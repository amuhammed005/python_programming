import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = [
            "How many elements are in the periodic table?",
            "Which animal lays the largest eggs?",
            "What is the most abundant gas in Earth's atmosphere?",
            "How many bones are in the human body?",
            "Which planet in the solar system is the hottest?",
            "What is the capital of France?",
            "Who painted the Mona Lisa?",
            "What is the square root of 144?",
            "What is the largest mammal in the world?",
            "What is the chemical symbol for gold?",
        ]
        self.options = [
            ["116", "117", "118", "119"],
            ["Whale", "Crocodile", "Elephant", "Ostrich"],
            ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"],
            ["206", "207", "208", "209"],
            ["Mercury", "Venus", "Earth", "Mars"],
            ["Berlin", "Rome", "Paris", "Madrid"],
            ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            ["10", "12", "14", "16"],
            ["Blue Whale", "Elephant", "Giraffe", "Orca"],
            ["Au", "Ag", "Fe", "Hg"],
        ]
        self.answers = ["118", "Ostrich", "Nitrogen", "206", "Venus", "Paris", "Leonardo da Vinci", "12", "Blue Whale", "Au"]
        self.current_question = 0
        self.score = 0

        # Widgets
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.options_frame, text="", font=("Arial", 12), command=lambda idx=i: self.check_answer(idx))
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.option_buttons.append(btn)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=f"Q{self.current_question + 1}: {self.questions[self.current_question]}")
            for idx, option in enumerate(self.options[self.current_question]):
                self.option_buttons[idx].config(text=option)
        else:
            self.show_result()

    def check_answer(self, idx):
        selected_option = self.options[self.current_question][idx]
        correct_answer = self.answers[self.current_question]
        if selected_option == correct_answer:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")

        self.current_question += 1
        self.root.after(1500, self.load_question)

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.questions)}")
        self.root.destroy()

# Main App
root = tk.Tk()
app = QuizApp(root)
root.mainloop()

