#Function to create starting screen
def starting_screen():
  import time
  import os
  print(
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
  return(0)

#Function to create a how to play screen
def how_to_play():
  import time
  import os
  print('\n\t\t\t ___________________'
      '\n\t\t\t/                   \ ' 
      '\n\t\t   |     HOW TO PLAY     |'
      '\n\t\t\t\___________________/')
  print('\n\nPlay against a CPU or a friend to conquer the waters')
  print('\nIn a 8 by 8 grid, guess the coordinants of your opponents battleships and destroy them')
  print('\nBoth players will have 7 battleships')
  print('\nThe first one to destroy all enemy battleships wins')
  time.sleep(8)
  os.system('clear')
  return(0)

#Function to create a loading screen
def loading_screen():
  import time
  import sys
  import os
  for x in range (0,4):
    z = ("Loading" + "." * x)
    sys.stdout.write('\r'+z)
    time.sleep(0.5)
  time.sleep(1)
  os.system('clear')
  print("\n _____  ___  _   _ _   _ _____ _   _ _____    ___ _____   _____ _   _ _____  ______ _____ ___ ________   __"
"\n/  __ \/ _ \| \ | | \ | |  _  | \ | /  ___|  / _ \_   _| |_   _| | | |  ___| | ___ \  ___/ _ \|  _  \ \ / /"
"\n| /  \/ /_\ \  \| |  \| | | | |  \| \ `--.  / /_\ \| |     | | | |_| | |__   | |_/ / |__/ /_\ \ | | |\ V / "
"\n| |   |  _  | . ` | . ` | | | | . ` |`--. \ |  _  || |     | | |  _  |  __|  |    /|  __|  _  | | | | \ /  "
"\n| \__/\ | | | |\  | |\  \ \_/ / |\  /\__/ / | | | || |     | | | | | | |___  | |\ \| |__| | | | |/ /  | |  "
 "\n \____|_| |_|_| \_|_| \_/\___/\_| \_|____/  \_| |_/\_/     \_/ \_| |_|____/  \_| \_\____|_| |_/___/   \_/  ")
  time.sleep(3)
  os.system('clear')
                                                                                                                                                          