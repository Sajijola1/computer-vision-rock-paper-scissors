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
            print(f"{countdown_time - count}!")
            # Add 1 to the count
            count += 1
    
    print("Go! ")

countdown_timer(5)

"""
You should call the function time() to create a countdown
In the previous task, the script reads the input from the camera and then compares it with the computer's choice without stopping. 
However, when you play a regular game, you usually count down to zero, and at that point you show your hand.
In this case, you need to add that countdown. 
An important thing to remember is that you can't use the sleep function because it will stop the script, 
and during that time, the camera will not be able to capture the input. 
Use the function time.time() to get how much time has passed since the script started. 
Print, for example, "you chose rock" in the terminal when the countdown gets to zero.
"""