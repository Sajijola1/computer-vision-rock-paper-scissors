import random

# Randomly picks an option from "Rock", "Paper" or "Scissors" for the computer
def get_computer_choice():
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    # Return the computer's choice
    return computer_choice

# Ask the user for an input and return it
def get_user_choice():

    user_choice = input('Kindly choose between "Rock", "Paper" or "Scissors": ')
    return user_choice