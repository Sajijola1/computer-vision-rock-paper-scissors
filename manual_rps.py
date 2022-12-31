import random
import time

def countdown_timer(countdown_time):
    """ A simple timer that implements a countdown in python without using the time.sleep() funciton.
    Takes the countown duration in seconds as an argument.
    Prints each second of execution to the console and returns the total execution time to the user"""
    
    # Store the start time
    start_time = time.time()
    
    # Create a counter variable. We don't want this to be in the while loop or it resets back to with each iteration 
    count = 0
    
    # Inform the user of the countdown
    print("Starting Countdown")

    while True:
        # After 1 sec
        if (time.time() - start_time) == 1.00:
            # Reset the start time
            start_time = time.time()

            # Check if the count is equal to the maximum time specified        
            # if round(time.time() - start_time, 2) + count == max_time:
            if count == countdown_time:     # quicker condition
                break   # break out of the loop
            print(countdown_time - count)
            # Add 1 to the count
            count += 1
    
    print("Go! ")

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
        print("Computer chose Rock")
        print("You won!")
    
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("Computer chose Rock")
        print("You lost")
    
    elif computer_choice == "Rock" and user_choice == "Rock":
        print("Computer chose Rock")
        print("It is a tie!")
    
    elif computer_choice == "Paper" and user_choice == "Paper":
        print("Computer chose Paper")
        print("It is a tie!")
    
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print("Computer chose Paper")
        print("You won!")
        
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("Computer chose Paper")
        print("You lost")

    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("Computer chose Scissors")
        print("You lost")
    
    elif computer_choice == "Scissors" and user_choice == "Scissors":
        print("Computer chose Scissors ")
        print("It is a tie!")
        
    elif computer_choice == "Scissors" and user_choice == "Rock":
        print("Computer chose Scissors")
        print("You won!")

# Running the game
def play():
    countdown_timer(3)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    return get_winner(computer_choice, user_choice)

play()

