import tkinter as tk
from tkinter import messagebox
from random import shuffle

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Paris", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "Which gas do plants primarily use for photosynthesis?",
                "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "correct_answer": "Carbon Dioxide"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Fe", "Cu"],
                "correct_answer": "Au"
            }
            # Add more questions here
        ]
        self.score = 0
        self.current_question = 0
        self.shuffle_questions()
        self.create_widgets()

    def shuffle_questions(self):
        shuffle(self.questions)

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Helvetica", 10, "bold"), command=lambda i=i: self.check_answer(i))
            self.answer_buttons.append(button)
            button.pack(pady=5, padx=20, fill=tk.X)

        self.next_button = tk.Button(self.root, text="Next", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Helvetica", 12), command=self.play_again)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, choice in enumerate(question_data["choices"]):
                self.answer_buttons[i].config(text=choice, state=tk.NORMAL, bg="lightgray")
            self.next_button.config(state=tk.DISABLED)
            self.score_label.config(text="")
        else:
            self.show_final_results()

    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question]
        selected_answer = question_data["choices"][selected_index]
        correct_answer = question_data["correct_answer"]

        for i, button in enumerate(self.answer_buttons):
            if i == selected_index:
                if selected_answer == correct_answer:
                    button.config(bg="palegreen")
                    self.score += 1
                else:
                    button.config(bg="lightcoral")
            elif question_data["choices"][i] == correct_answer:
                button.config(bg="palegreen")

        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)
        
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_final_results(self):
        self.question_label.config(text="Quiz Complete!")
        self.score_label.config(text=f"Your Score: {self.score}/{len(self.questions)}")
        self.next_button.pack_forget()
        self.play_again_button.pack(pady=10)

    def play_again(self):
        self.current_question = 0
        self.score = 0
        self.shuffle_questions()
        self.show_question()
        self.play_again_button.pack_forget()
        self.next_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()
