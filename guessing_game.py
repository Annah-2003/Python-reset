import random
import tkinter as tk
from tkinter import messagebox

def generate_number():
    return random.randint(1, 100)

def check_guess(number, guess):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Congratulations! You guessed it!"

def check_guess_and_update_label():
    guess = int(guess_entry.get())
    feedback = check_guess(number_to_guess, guess)
    feedback_label.config(text=feedback)

def main():
    global number_to_guess
    number_to_guess = generate_number()

    root = tk.Tk()
    root.title("Guessing Game")

    guess_label = tk.Label(root, text="Enter your guess:")
    guess_label.pack()

    guess_entry = tk.Entry(root)
    guess_entry.pack()

    check_button = tk.Button(root, text="Check", command=check_guess_and_update_label)
    check_button.pack()

    feedback_label = tk.Label(root, text="")
    feedback_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
