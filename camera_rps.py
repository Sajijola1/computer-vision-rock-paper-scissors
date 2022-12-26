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

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    
    cv2.imshow('frame', frame)
    
    # Have the model predict what the current image is. Model.predict
    # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
    # it is the first label and 80% sure its the second label.
    probabilities = model.predict(data)
    # Print the label of the highest probability
    prediction = labels[np.argmax(probabilities)]
    # print(prediction[2:])

    def get_computer_choice():
        """Randomly picks an option from "Rock", "Paper" or "Scissors" for the computer
        and returns the computer's choice.
        
        Arguments: None"""
        
        # Return the computer's choice
        return random.choice(["Rock", "Paper", "Scissors"])

    def get_user_choice():
        """Ask the user to choose between "Rock", "Paper" or "Scissors" as
        an input, and returns the user's choice
        
        Arguments: None"""

        return prediction[2:]
        #return input('Kindly choose between "Rock", "Paper" or "Scissors": ')

    def get_winner(computer_choice, user_choice):
        """Compares the user and computer's choices and chooses a winner
        based on logic of the Rock-paper-scissors game
        
        Arguments:

        computer_choice(str) -> A string representing the choice of the computer
        
        user_choice(str) -> A string representing the choice of the user"""
        
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

        else:
            print("Choose an option")

    # Running the game
    def play():
        user_choice = get_user_choice()
        # print(user_choice)
        computer_choice = get_computer_choice()
        # print(computer_choice)

        return get_winner(computer_choice, user_choice)

    play()

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()