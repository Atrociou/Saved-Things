import time


myWord = "hype"


choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

letter = input("Type a letter: ")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")
	
	count = 0 
	for l in myWord:
		if l == letter:
			print(count)
	count += 1

myWord = list(myWord)

guessList = []
for a in myWord:
	guessList.append("_")
guessList[0] = "h"
print(guessList)


hangmanList = ['''
    +===+
        |
        |
        |
        |     
       ===''','''
    +===+
    0   |
        |
        |
        |
       ===	''','''
    +===+
    0	|
    |	|
    	|
    	|
       ===
				''','''
    +===+
    0   |
    |\  |
        |
        |     
       ===''','''
    +===+
    0   |
   /|\  |
        |
        |
       ===	''','''
    +===+
    0   |
   /|\  |
     \  |
        |
       ===	''','''
    +===+
    0	|
   /|\	|
   / \	|
    	|
       ===
				''']
				
				

misses = 0

while misses < 7:
	guess = input("Guess a letter: ")
	if guess in myWord:
		# Loop through myWord and change my guessList at the correct indexes
		print("Letter is in the word")
	else:
		misses += 1

print("Game Over")
 