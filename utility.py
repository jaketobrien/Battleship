# Lab 10
# EE115_Lab_10_Ex10.1_q1.py
# 11/12/2020 
# Create a function of a battleship game
# Authors: Sarah Byrne and Jake O'Brien
#This py file contains:
#The functions used in the main battleship function
#The main battleship function that runs the main body of the game 

#Function of starting screen
def starting_screen():
  '''Function that prints the starting screen of game'''
  import time #import time module to holf someting on screen for certain time
  import os #import os module to clear screen
  print(  #starting screen print
  "\n  ________________________________________________________"
  "\n /                                                        \ "
  "\n|  ______         _    _    _             _      _         |"      
  "\n|  | ___ \       | |  | |  | |           | |    (_)        |"       
  "\n|  | |_/ /  __ _ | |_ | |_ | |  ___  ___ | |__   _  _ __   |"
  "\n|  | ___ \ / _` || __|| __|| | / _ \/ __|| '_ \ | || '_ \  |"
  "\n|  | |_/ /| (_| || |_ | |_ | ||  __/\__ \| | | || || |_) | |"
  "\n|  \____/  \__,_| \__| \__||_| \___||___/|_| |_||_|| .__/  |"
  "\n|                                                  | |     |"
  "\n|                                                  |_|     |"
  "\n \________________________________________________________/")
  print('\n\n\t\t\t\tPlease widen screen fully')
  input('\n\n\t\t\t Press <Enter> to start the game\n\n\t\t\t\t\t\t\t')
  time.sleep(.0001)
  os.system('clear') 


#Function of how to play
def how_to_play():
  '''Function that prints information on how to play the battleship game'''
  import time
  import os
  print('\n\t\t\t ___________________'    #how to play screen
      '\n\t\t\t/                   \ ' 
      '\n\t\t   |     HOW TO PLAY     |'
      '\n\t\t\t\___________________/')
  print('\n\nPlay against a CPU or a friend to conquer the waters')
  print('\nIn a 8 by 8 grid, guess the coordinates of your opponents battleships and destroy them')
  print('\nBoth players will have 7 battleships')
  print('\nThe first one to destroy all enemy battleships wins')
  time.sleep(8)
  os.system('clear')
  return(0)

#Function of loading screen
def loading_screen():
  '''Function that prints the battleship game loading screen'''
  import time
  import sys  #import sys module, provides functions and variables used to manipulate different parts of the runtime
  import os
  for x in range (0,4): #for x in range 0 to 4
    z = ("Loading" + "." * x) #z equals word "loading" and a dot multiplied by the amount of runs at that time, i.e. 3 runs 3 dots
    sys.stdout.write('\r'+z)  #write loading and dots after one another
    time.sleep(0.5) #0.5 secs between dots
  time.sleep(1) #1 sec until clear
  os.system('clear')
  print("\n _____  ___  _   _ _   _ _____ _   _ _____    ___ _____   _____ _   _ _____  ______ _____ ___ ________   __"
"\n/  __ \/ _ \| \ | | \ | |  _  | \ | /  ___|  / _ \_   _| |_   _| | | |  ___| | ___ \  ___/ _ \|  _  \ \ / /"
"\n| /  \/ /_\ \  \| |  \| | | | |  \| \ `--.  / /_\ \| |     | | | |_| | |__   | |_/ / |__/ /_\ \ | | |\ V / "
"\n| |   |  _  | . ` | . ` | | | | . ` |`--. \ |  _  || |     | | |  _  |  __|  |    /|  __|  _  | | | | \ /  "
"\n| \__/\ | | | |\  | |\  \ \_/ / |\  /\__/ / | | | || |     | | | | | | |___  | |\ \| |__| | | | |/ /  | |  "
 "\n \____|_| |_|_| \_|_| \_/\___/\_| \_|____/  \_| |_/\_/     \_/ \_| |_|____/  \_| \_\____|_| |_/___/   \_/  ")
  time.sleep(3)
  os.system('clear')

#Function to assign ship which accepts the input N 
#N is the number of ship coordinates to be generated
def assign_ship(N):
  '''#Function to assign ship which accepts the input N. 
  N is the number of ship coordinates to be generated
  Function returns the number of ships and the locations of the ships in a list'''
  import random #import random module to randomise
  player_ships=[] 
  for ships in range(0,N):  #N ship locations are created
    x_point=random.randint(0,7)   #creating the y-coordinate
    y_point=random.randint(0,7)   #creating the x-coordinate
    while (x_point,y_point) in player_ships:  #while (x,y) is in player's ships, new points will be generated
      x_point=random.randint(0,7) 
      y_point=random.randint(0,7) 
    player_ships.append((x_point,y_point))  #append x and y points into ship location list
  numb_ships= N
  return (numb_ships,player_ships) # returns the number of ships and ship coordinates

#Function to print the player's battleboard 
#Function takes in the players name, the number of ships, the ship coordinates and the computer guess history
def player_battleship_board(name_of_player1,numb_ships,player_ships,computer_guess_history):
  '''Function to print the player's battleboard.
  Function takes in the players name, the number of ships, the ship coordinates and the computer guess history'''
  print('\n',name_of_player1,'\n__________')
  print(name_of_player1,'has',numb_ships,'ships remaining') #Displays number of ships left
  for y in range(7,-1,-1):   #creating the y-coordinate
    for x in range(8):       #creating the x-coordinate
      points=(x,y)           #board is an 8x8 from 0 to 7
      if (points in player_ships) and (points not in computer_guess_history):   #If coordinates are in ship locations 
        print('\u26F4', end='   ')                                               #and haven't been guessed - ship is printed
      elif (points in player_ships) and (points in computer_guess_history):     #If coordinates are in ship locations
        print('\U0001F525', end='   ')                                            #and have been guessed - fire is printed
      elif (points not in player_ships) and (points in computer_guess_history):  #If coordinates are not in ship locations
        print('\u274C', end='   ')                                                 #and have been guessed - a miss 'X' is printed 
      else:                                                                      #If anything else - a target is printed
        print('\u25CE', end='   ')
    print('')
  return('___________________________________')

#Function to print the computer's battleboard 
#Function takes in the players name, the number of ships, the ship coordinates and the player guess history
def computer_battleship_board(name_of_player2,numb_ships,player_ships,player_guess_history):
  '''Function to print the computers's battleboard 
  Function takes in the players name, the number of ships, the ship coordinates and the player guess history'''
  print('\n',name_of_player2,'\n__________')
  print(name_of_player2,'has',numb_ships,'ships remaining')  #Displays number of ships left
  for y in range(7,-1,-1):     #creating the y-coordinate
    for x in range(8):         #creating the x-coordinate
      points=(x,y)             #board is an 8x8 from 0 to 7
      if (points in player_guess_history) and (points in player_ships):          #If coordinates are in ship locations
        print('\U0001F525', end='   ')                                             #and have been guessed - fire is printed
      elif  (points not in player_ships) and (points in player_guess_history):   #If coordinates are not in ship locations
        print('\u274C', end='   ')                                                 #and have been guessed - a miss 'X' is printed 
      else:                                                                      #If anything else - a target is printed
        print('\u25CE', end='   ')
    print('')
  return('___________________________________')

#Function that requests an x,y coordinate from the user and appends this coordinate to the player guess history
#Function takes in the player guess history
def player_guess(player1_guess_history):
  '''Function that requests an x,y coordinate from the user and appends this coordinate to the player guess history.
  Function takes in the player guess history.
  Function returns the x,y coordinate of the player's guess.'''
  input_coordinates= input('Enter a target co-ordinate: ')  #accepts coordinate
  (x,y) = tuple(map(int, input_coordinates.split(',')))     #turns coordinate into a tuple
  while ((x<0 or x>7) or (y<0 or y>7)) or (x,y) in player1_guess_history:  #loop ensures that the coordinate is inside the 8x8 board and not guessed
    if ((x<0 or x>7) or (y<0 or y>7)) :                    #ensures that the coordinate is inside the 8x8 board
      print('Please enter co-ordinates inside the battlefield')
      input_coordinates= input('Enter a target co-ordinate: ')
      (x,y) = tuple(map(int, input_coordinates.split(',')))
    elif (x,y) in player1_guess_history:                    #ensures that the coordinate has not already been guessed
      print('Please enter new co-ordinates')
      input_coordinates= input('Enter a target co-ordinate: ')
      (x,y) = tuple(map(int, input_coordinates.split(',')))
  player1_guess_history.append((x,y))    #adds the coordinate to the player guess history
  print('Firing at',(x,y))
  return((x,y))   #function returns the guess inputed 

#Function that generates an x,y coordinate and appends this coordinate to the computer guess history
#Function takes in the computer guess history
def computer_guess(computer_guess_history):
  '''Function that generates an x,y coordinate and appends this coordinate to the computer guess history.
  Function takes in the computer guess history.
  Function returns the x,y coordinate of the player's guess.'''
  import random
  print('Computer is generating target co-ordinates ')
  x = random.randint(0,7)               #creating the x-coordinate
  y = random.randint(0,7)               #creating the y-coordinate
  guess=(x,y)
  while (x,y) in computer_guess_history:  #while (x,y) has already been guessed, new points will be generated
    x = random.randint(0,7)
    y = random.randint(0,7)
    guess=(x,y)
  computer_guess_history.append(guess) #adds the coordinate to the player guess history
  print('Firing at',guess)
  return (guess)   #function returns the guess generated 

#Function that checks if the x,y coordinate guess is one of the opponent's ship location
#Function takes in the guess, the ship coordinates, and the number of ships
def check_player_guess(guess,computer_ships,numb_ships):
  '''Function that checks if the x,y coordinate guess is one of the opponent's ship location.
  Function takes in the guess, the ship coordinates, and the number of ships.
  Function updates the number of ships left.'''
  import time
  if guess in computer_ships:  #If the coordinate is a ship location 1 is taken away
    time.sleep(3)               #from the count of number of opponent ships
    hit_screen()                #and the graphic for hit prints
    numb_ships-=1  
  else:                         #If the coordinate is not a ship location it is a miss
    print('It was a miss')
    time.sleep(3)
  return(numb_ships)       #Function returns the updated number of ships the opponent has

#Function that checks if the x,y coordinate guess is one of the opponent's ship location
#Function takes in the guess, the ship coordinates, and the number of ships
def check_computer_guess(guess,player1_ships,numb_ships):
  '''Function that checks if the x,y coordinate guess is one of the opponent's ship location.
  Function takes in the guess, the ship coordinates, and the number of ships.
  Function updates the number of ships left.'''
  import time
  if guess in player1_ships:     #If the coordinate is a ship location 1 is taken away
    time.sleep(3)                 #from the count of number of opponent ships
    hit_screen()                  #and the graphic for hit prints
    numb_ships-=1
  else:
    print('It was a miss')       #If the coordinate is not a ship location it is a miss
    time.sleep(3)
  return(numb_ships)         #Function returns the updated number of ships the opponent has

#Function of ship hit graphics used when a ship is hit
def hit_screen():
  '''Function of ship hit graphic sequence used when a ship is hit'''
  import os
  import time
  os.system('clear')
  print("\n"
  "\n"
  "\n"
  "\n"
  "\n     \U0001F4A3 "
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n"
  "\n         \U0001F4A3"
  "\n"
  "\n "
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n             \U0001F4A3"
  "\n"
  "\n"
  "\n"
  "\n "
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n                 \U0001F4A3"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n"
  "\n                       \U0001F4A3 "
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n"
  "\n"
  "\n"
  "\n                          \U0001F4A3 "
  "\n"
  "\n"
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n                             \U0001F4A3 "
  "\n"
  "_______________________________\u26F4____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "_______________________________\U0001F4A5____________")
  time.sleep(0.5)
  os.system('clear')
  print("\n"
  "\n                         _   _ _____ _____ _ _ "                                            
  "\n                        | | | |_   _|_   _| | |  "                                          
  "\n                        | |_| | | |   | | | | | "                                           
  "\n                        |  _  | | |   | | | | |   "                                         
  "\n                        | | | |_| |_  | | |_|_|  "                                          
  "\n                        \_| |_/\___/  \_/ (_|_)   "                                         
  "\n"                                                                                             
  "\n"                                                                                             
  "\n"                                                                                           
  "\n"                                                                                             
  "\n  _____ _   _ ___________  ______ _____ _____ ___________  _______   _____________ "
  "\n /  ___| | | |_   _| ___ \ |  _  \  ___/  ___|_   _| ___ \|  _  \ \ / /  ___|  _  \ "
  "\n \ `--.| |_| | | | | |_/ / | | | | |__ \ `--.  | | | |_/ // | | |\ V /| |__ | | | | "
  "\n  `--. \  _  | | | |  __/  | | | |  __| `--. \ | | |    / | | | | \ / |  __|| | | | "
  "\n /\__/ / | | |_| |_| |     | |/ /| |___/\__/ / | | | |\ \ \ \_/ / | | | |___| |/ / "
  "\n \____/\_| |_/\___/\_|     |___/ \____/\____/  \_/ \_| \_| \___/  \_/ \____/|___/  ")
  time.sleep(3)
  os.system('clear')
  

#Function that updates the score board in the file if the player wins the game
#Function takes in the players score
def score_board(score): 
  '''Function that updates the score board in a score board file.
  Function takes in the players score'''
  print('Enter your name and a message and see if you are one of the top 5 champions')
  score=str(score)
  name_input=input('\n\nEnter your name: ' )
  message_input=input('\nEnter a message: ' )
  print('\n')
  with open ('./lab10_champions.txt','r') as file: #opening the file and appending each line into a list
    my_list = []                       
    for line in file:
      my_list.append(line)
  past_champions=[]      #creating empty list that will contain previous player scores
  for n in range(5,10):
    past_champions.append(my_list[n])   #appending the previous players scores and information from file to new list
  new_player= str(score+'\t'+name_input+'    '+message_input+'\n') #creating new player information
  past_champions.append(new_player)       #adding new player information to new list
  past_champions.sort(key=lambda x:int(x[:3])) #sorting the player position by their score
  del past_champions[5]                        #deleting the last player on the list since it is a top 5 list
  with open ('./lab10_champions.txt','w') as file: #opening the file and writing the updated information 
    for n in range(0,5):
      file.write(my_list[n])
    for n in range(0,5):
      file.write(past_champions[n])
  with open ('./lab10_champions.txt','r') as file: #opening the file and printing the contents to screen
    print(file.read())
  return('\nCan you beat the champions')

#Main function that runs the battleship game using various functions
def battleship():
  '''Main function that runs the battleship game'''
  import time
  import os
  with open('./lab10_champions.txt','r') as file:   #printing the score board at the start of game 
    print(file.read())  
  starting_screen()          #printing the start screen, how to play directions and a loading screen
  how_to_play()
  loading_screen()
  playerships=assign_ship(7)      #The player is assigned 7 ship locations
  computerships=assign_ship(7)    #The computer is assigned 7 ship locations
  numb_player_ship=playerships[0]          #The number of ships the player has is assigned a name
  player_ship_loctaion=playerships[1]      #The location of the player's ships are assign a name
  numb_computer_ship=computerships[0]      #The number of ships the player has is assigned a name
  computer_ship_loctaion=computerships[1]  #The location of the computers's ships are assign a name
  player_history=[]              #Empty lists are created to store the player's and computer's guess history
  computer_history=[]
  print('Player ships locations:',player_ship_loctaion)
  print(player_battleship_board('Player',numb_player_ship,player_ship_loctaion,computer_history)) #printing the player's and computer's batttleship boards
  print(computer_battleship_board('Computer',numb_computer_ship,computer_ship_loctaion,player_history))
  while (numb_player_ship>0) and (numb_computer_ship>0): #while loop keeps looping until all of one player's ships are destroyed
    print('\n')
    player_guess1=player_guess(player_history)   #function allows the player to guess and returns the players guess and their guess history
    numb_computer_ship=check_player_guess(player_guess1,computer_ship_loctaion,numb_computer_ship)
    os.system('clear')
    print('Player ships locations:',player_ship_loctaion)
    print(player_battleship_board('Player',numb_player_ship,player_ship_loctaion,computer_history))
    print(computer_battleship_board('Computer',numb_computer_ship,computer_ship_loctaion,player_history))
    print('\n')
    #Player wins if all computer ships are destroyed
    if numb_computer_ship==0:
      os.system('clear')
      print("\n"
      "\n__   _______ _   _   _    _  _____ _   _   _ _ "
      "\n\ \ / /  _  | | | | | |  | ||  _  | \ | | | | |"
      "\n \ V /| | | | | | | | |  | || | | |  \| | | | |"
      "\n  \ / | | | | | | | | |/\| || | | | . ` | | | |"
      "\n  | | \ \_/ / |_| | \  /\  /\ \_/ / |\  | |_|_|"
      "\n  \_/  \___/ \___/   \/  \/  \___/\_| \_/ (_|_)")
      score=len(player_history)   #The player's score is equal to the number of guesses made
      print(score_board(score)) #If player wins then they can see if they make the score board
      time.sleep(4)
      break
    computer_guess1=computer_guess(computer_history)   #function returns the computer's guess and their guess history
    time.sleep(3)
    numb_player_ship=check_computer_guess(computer_guess1,player_ship_loctaion,numb_player_ship) #function returns number of ships the player has left
    os.system('clear')
    print('Player ships locations:',player_ship_loctaion)
    print(player_battleship_board('Player',numb_player_ship,player_ship_loctaion,computer_history))
    print(computer_battleship_board('Computer',numb_computer_ship,computer_ship_loctaion,player_history))
    #Computer wins if all player ships are destroyed
    if numb_player_ship==0:
      os.system('clear')
      print("\n"
      "\n__   _______ _   _   _     _____ _____ _____   _ _" 
      "\n\ \ / /  _  | | | | | |   |  _  /  ___|_   _| | | |"
      "\n \ V /| | | | | | | | |   | | | \ `--.  | |   | | |"
      "\n  \ / | | | | | | | | |   | | | |`--. \ | |   | | |"
      "\n  | | \ \_/ / |_| | | |___\ \_/ /\__/ / | |   |_|_|"
      "\n  \_/  \___/ \___/  \_____/\___/\____/  \_/   (_|_)")
      time.sleep(3)
      break
  print("\n"
  "\n _____   ___  ___  ___ _____   _____  _   _ ___________ "
  "\n|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ "
  "\n| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /"
  "\n| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / "
  "\n| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ "
  "\n \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|")
  time.sleep(3)
  os.system('clear')