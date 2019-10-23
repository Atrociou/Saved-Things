import time
import os

frameList = ['''
   () ()
    \|/
   / | \
              ''','''
  
 \ \ \  \ 
   +   +
  \  |  /
    /_\
   |   |
  ''','''

 _/\_/\_
 :: ::  |
  ;;    |
 -, -, -|


						''']
   



#   +---+
 #	0   |
 #  /|\  |
 #  / \  |
 #      === ''', '''

 #   +---+
 #  \0/ | 
 #   |  |
 #   \\\\ |
 #      ==='''

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.7)