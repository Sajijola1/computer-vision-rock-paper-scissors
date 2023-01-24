import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

import time
import random
import cv2
from keras.models import load_model
import numpy as np

# Create a class for the rock-paper-scissors game
class RockPaperScissors():
    def __init__(self) -> None:
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Grab the labels from the labels.txt file. This will be used later.
        self.labels = open('labels.txt', 'r').readlines()
        # print(labels)



    # Use a lambda function to get random computer choice
    get_computer_choice = lambda self: random.choice(["Rock", "Paper", "Scissors"])

    def countdown_timer(self, countdown_time, message1=str, message2=str):
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

    def get_prediction(self, countdown_time):
        
        # Inform the user of the countdown
        # print(message1)

        while True:

            ret, frame = self.cap.read()
            cv2.imshow('frame', frame)

            # Store the start time
            start_time = time.time()

            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image

            while (countdown_time) > 0:
                ret, frame = self.cap.read()
                cv2.putText(frame, 
                "Display your choice to the camera and press 'q' \nTime left: " 
                + str(countdown_time), (0, 35), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), cv2.LINE_4)
                cv2.imshow('frame', frame)

                cur = time.time()
                
                if cur-start_time >= 1:    
                    start_time = cur
                    countdown_time -= 1
            

            # Have the model predict what the current image is
            probabilities = self.model.predict(self.data)
            # Print the label of the highest probability
            prediction = self.labels[np.argmax(probabilities)]
            # Remove the first two characters and newline from the label e.g '0 Rock\n'
            prediction = prediction[2:-1]

            # Press q to close the window
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break

        return prediction

# Checks the user and computer choices and chooses a winner.
    def get_winner(self, computer_choice=str, user_choice=str):

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
    def play(self):
        
        # Store number of user and computer wins
        computer_wins = 0
        user_wins = 0

        # store number of rounds played
        rounds_played = 0

        while True:

            user_choice = self.get_prediction(5)
            computer_choice = self.get_computer_choice()

            winner = self.get_winner(computer_choice, user_choice)

            #TODO: Try => prompt = input("press Enter to continue or "exit" to end game... ")
            #TODO: Try => if (user_wins or computer_wins) >= 3 or rounds_played >= 5 or prompt.lower() == "exit":
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

            
            if (user_wins or computer_wins) >= 3 or rounds_played >= 5:

                # Prompt the player to play another round
                replay = input("Game over, Would you like to play again(y/n): ").lower()

                # Use recursion to start the game again
                if replay == "y":
                    self.play()  
                    break

                # Display the overall winner
                else:
                    if computer_wins > user_wins:
                        print("Computer wins!")
                        print("Thanks for playing")
                        break
                    elif computer_wins == user_wins:
                        print("You drew with the computer")
                        print("Thanks for playing")
                        break
                    else:
                        print("You win!")
                        print("Thanks for playing")
                        break

        # Release the cap object when game ends
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

Player1 = RockPaperScissors()
Player1.play()