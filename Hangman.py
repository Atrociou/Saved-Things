import time
import os

myWord = "hype"


choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

Letter = input("Type a letter: ")
if Letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")
	count = 0 
	for l in myWord:
		if l == Letter:
			print(count)
	count += 1

hangmanList = ['''
    +===+
        |
        |
        |
        |     
       ===
       			''']



myWord = list("hype")
guessList = list("____")

index = 0

for letter in myWord:
	if letter == Letter:
		guessList[index] = Letter
	index += 1
print(guessList)



#guessList = []
#for a in myWord:
#	guessList.append("_")
#guessList[0] = "h"
#print(guessList)

misses = 0

while misses < 7:
	guess = input("Guess a letter: ")
	if guess in myWord:
		# Loop through myWord and change my guessList at the correct indexes
		print("Letter is in the word")
	else:
		misses += 1
		
print("Game Over")









