import random

# Randomly picks an option from "Rock", "Paper" or "Scissors" for the computer
def get_computer_choice():
    
    # Return the computer's choice
    return random.choice(["Rock", "Paper", "Scissors"])

# Ask the user for an input and return it
def get_user_choice():

    return input('Kindly choose between "Rock", "Paper" or "Scissors": ')

# Checks the user and computer choices and chooses a winner.
def get_winner(computer_choice, user_choice):
    
    if computer_choice == "Rock" and user_choice == "Paper":
        print("You won!")
    
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost")
    
    elif computer_choice == "Rock" and user_choice == "Rock":
        print("It is a tie!")
    
    elif computer_choice == "Paper" and user_choice == "Paper":
        print("It is a tie!")
    
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print("You won!")
        
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost")

    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost")
    
    elif computer_choice == "Scissors" and user_choice == "Scissors":
        print("It is a tie!")
        
    elif computer_choice == "Scissors" and user_choice == "Rock":
        print("You won!")

# Running the game
def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    return get_winner(computer_choice, user_choice)

play()
