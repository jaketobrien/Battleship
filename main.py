# Authors: Jake O'Brien and Sarah Byrne
# Date: 11/12/2020
# Description: The battleship function that runs the main body of the game using the functions from utility.py.  
#              The play game function which runs the battleship function in a loop until the user does not want to play

import utility as function #Importing the functions from the utility file
#help(function)

# Function of then battleship game in a loop that keeps repeating till the user does not want to play
def play_game():
  import os 
  while True:  #loop will continue while true
    os.system('clear')  #makes sure the screen is clear before the body of the loop is carried out
    print("\n\n\n\t\tCreators: Sarah Byrne and Jake O'Brien")
    input_Y_or_N=input("\n\n\n\t\t\u23F3  Type 'Y' to play or 'N' to quit \u23F3\n\n\t\t\t\t\t\t ")
    input_Y_or_N.lower()
    if input_Y_or_N.lower()=='y': #if input==y the game will be carried out
      os.system('clear')    #clears the screen before game starts         
      print(function.battleship()) #playing the game
    else:
      input_Y_or_N.lower()=='n'   #loop will only end if input==n and the function to play the game stops
      os.system('clear')
      break

# Calling the function play_game
play_game()