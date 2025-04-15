import pyautogui
import random
import time
import keyboard
import threading

#a thread will be created to check for 'q' key press to exit the program, the mouse only moves when running is true
running = True

#gets the screen size so that the mouse can be moved to places within the screen
screen_width, screen_height = pyautogui.size()

#this is to create an adjustable area where the mouse can move to, this is to prevent the mouse from moving to the edge of the screen and causing an error of any sorts
amount_away_from_the_screen = 80

#this function checks for if the 'q' key is pressed, if it is pressed it sets running to false and exits the program
def check_for_exit():
    global running
    while running:
        if keyboard.is_pressed('q'):
            running = False
            print("Exiting...")

#a new thread is created using the check_for_exit function which will run in the background and check for the 'q' key press
exit_thread = threading.Thread(target=check_for_exit)

#starts the thread
exit_thread.start()

#runs before the 'q' key is pressed
while running:
    #gets random numbers for the mouse to move to
    #
    x = random.randint(amount_away_from_the_screen, screen_width - amount_away_from_the_screen)
    y = random.randint(amount_away_from_the_screen, screen_height - amount_away_from_the_screen)
    
    #the mouse moves to the random coordinates given by the x and y variables
    pyautogui.moveTo(x, y, 0.5)
    
    #waits for 2 seconds before moving the mouse to a random position again
    time.sleep(2)

#terminates the thread
exit_thread.join()