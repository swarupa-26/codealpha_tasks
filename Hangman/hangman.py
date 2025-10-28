import tkinter as tk
import random

# --- Game Logic (Modified for GUI) ---
class HangmanGame:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")
        master.geometry("500x400")
        master.configure(bg="#f0f0f0")

        self.words = ['python', 'hangman', 'programming', 'computer', 'keyboard', 'apple', 'banana', 'bookkeeper']
        self.word = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        # Word display
        self.word_label = tk.Label(self.master, text="", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.word_label.pack(pady=20)

        # Status messages
        self.status_label = tk.Label(self.master, text="Welcome to Hangman!", font=("Arial", 14), bg="#f0f0f0")
        self.status_label.pack(pady=10)

        # Incorrect guesses count
        self.guesses_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.guesses_label.pack()
        
        # Guessed letters display
        self.guessed_letters_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.guessed_letters_label.pack()

        # Input field and button
        input_frame = tk.Frame(self.master, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        self.guess_entry = tk.Entry(input_frame, width=3, font=("Arial", 16), justify="center")
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", self.check_guess_event) # Allows guessing with Enter key

        self.guess_button = tk.Button(input_frame, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(side=tk.LEFT)

        # New Game button
        self.new_game_button = tk.Button(self.master, text="New Game", font=("Arial", 12), command=self.start_new_game)
        self.new_game_button.pack(pady=10)

    def start_new_game(self):
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.update_display()
        self.status_label.config(text="Welcome to Hangman!")
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal")

    def update_display(self):
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_label.config(text=display_word)
        self.guesses_label.config(text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
        self.guessed_letters_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def check_guess_event(self, event):
        self.check_guess()

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            self.status_label.config(text="Invalid input. Enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.status_label.config(text="You already guessed that letter. Try a new one.")
            return

        self.guessed_letters.append(guess)
        
        if guess in self.word:
            self.status_label.config(text="Good guess! 👍")
        else:
            self.status_label.config(text="Incorrect guess! ❌")
            self.incorrect_guesses += 1
            
        self.update_display()
        self.check_game_status()

    def check_game_status(self):
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        
        if "_" not in display_word:
            self.status_label.config(text=f"Congratulations! You've guessed the word correctly: {self.word}")
            self.end_game()
        elif self.incorrect_guesses >= self.max_incorrect_guesses:
            self.status_label.config(text=f"Game Over! The word was: {self.word}")
            self.end_game()

    def end_game(self):
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")

# --- Main Application ---
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
