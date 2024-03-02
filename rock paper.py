import tkinter as tk
from tkinter import messagebox
import random

def play():
    user_choice = user_selection.get()
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

def play_again():
    user_selection.set("")
    result_label.config(text="")
    play()

choices = ["rock", "paper", "scissors"]

root = tk.Tk()
root.title("Rock Paper Scissors Game")

user_selection = tk.StringVar()
user_selection.set("")

instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

user_entry = tk.Entry(root, textvariable=user_selection)
user_entry.pack()

play_button = tk.Button(root, text="Play", command=play)
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack()

root.mainloop()
