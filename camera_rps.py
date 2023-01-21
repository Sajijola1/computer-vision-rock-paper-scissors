import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

import time
import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Grab the labels from the labels.txt file. This will be used later.
labels = open('labels.txt', 'r').readlines()
# print(labels)

def get_computer_choice():
    """
    Randomly picks an option from "Rock", "Paper" or "Scissors" for the computer
    
    and returns the computer's choice.
    
    Arguments:
    ---
    None
    """
    
    # Return the computer's choice
    return random.choice(["Rock", "Paper", "Scissors"])

def countdown_timer(countdown_time, message1=str, message2=str):
    """ 
        A simple timer that implements a countdown in python without using the time.sleep() funciton.
    
        Takes the countown duration in seconds and two messages as arguments.
    
    Prints:
    -------
        The first message before the countdown starts,
        
        Each elapsed second during the countdown and 
        
        The final message at the end of the countdown
    
    """

    # Create a counter variable. We don't want this to be in the while loop or it resets back to 0 with each iteration 
    count = 0
    
    # Inform the user of the countdown
    print(message1)
    
    # Store the start time
    start_time = time.time()
    
    while True:
        # After 1 sec
        if (time.time() - start_time) == 1.00:
            # Reset the start time
            start_time = time.time()

            # Check if the count is equal to the maximum time specified
            if count == countdown_time:     # quicker condition
                break   # break out of the loop
            print(f"{countdown_time - count}!")
            # Add 1 to the count
            count += 1
    
    # Print prompt
    print(message2)

def get_prediction():

    # Call the Countdown function with messages for the game
    # countdown_timer(3,"Get ready", "Display your choice to the camera")

    while True:

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image

        cv2.imshow('frame', frame)

        # Have the model predict what the current image is
        probabilities = model.predict(data)
        # Print the label of the highest probability
        prediction = labels[np.argmax(probabilities)]
        # Remove the first two characters and newline from the label e.g '0 Rock\n'
        prediction = prediction[2:-1]

        # Press q to close the window
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    return prediction

# Checks the user and computer choices and chooses a winner.
def get_winner(computer_choice=str, user_choice=str):

    if computer_choice == "Rock":
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        if user_choice == "Paper":
            print("You won!")
            winner = "User"
        elif user_choice == "Scissors":
            print("You lost")
            winner = "Computer"
        elif user_choice == "Rock":
            print("It is a tie!") 
            winner = "Tie"
        else:
            winner = None
            print("Please show a valid choice to the camera...") 
    
    elif computer_choice == "Paper":
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        if user_choice == "Paper":
            print("It is a tie!")
            winner = "Tie"
        elif user_choice == "Scissors":
            print("You won!")
            winner = "User"
        elif user_choice == "Rock":
            print("You lost")
            winner = "Computer"
        else:
            winner = None
            print("Please show a valid choice to the camera...")

    elif computer_choice == "Scissors":
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        if user_choice == "Paper":
            print("You lost")
            winner = "Computer"
        elif user_choice == "Scissors":
            print("It is a tie!")
            winner = "Tie"     
        elif user_choice == "Rock":
            print("You won!")
            winner = "User"
        else:
            winner = None
            print("Please show a valid choice to the camera...")

    return winner

# Running the game
def play():

    # Store number of user and computer wins
    computer_wins = 0
    user_wins = 0

    # store number of rounds played
    rounds_played = 0

    while True:

        if (user_wins and computer_wins) < 3 and rounds_played < 5:
            user_choice = get_prediction()
            computer_choice = get_computer_choice()

            winner = get_winner(computer_choice, user_choice)

            if winner == "Computer":
                # Increase the count for the rounds played
                rounds_played += 1
                # Add to the number of computer wins
                computer_wins += 1
                input("press Enter to continue... ")

            elif winner == "User":
                # Increase the count for the rounds played
                rounds_played += 1
                # Add to the number of user wins
                user_wins += 1
                input("press Enter to continue... ")

            elif winner == "Tie":
                # Increase the count for the rounds played
                rounds_played += 1
                input("press Enter to continue... ")

            else:
                print("You did not choose an option, please try again...")
                # Increase the count for the rounds played
                rounds_played += 1
                input("press Enter to continue... ")

        else:

            # Display the overall winner
            replay = input("Would you like to play again(y/n): ").lower()

            if replay == "y":
                play()  # Use recursion to start the game again
                break

            else:
                if computer_wins > user_wins:
                    print("Game over, Computer wins")
                    print("Thanks for playing")
                    break
                elif computer_wins == user_wins:
                    print("Game over\n You drew with the computer")
                    print("Thanks for playing")
                    break
                else:
                    print("Game over, You win!")
                    print("Thanks for playing")
                    break

    # Release the cap object when game ends
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

play()