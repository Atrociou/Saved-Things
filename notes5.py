myWord = "hello"
if choice == myWord 
		print("its a match")
else:
		print("not am amtch")
# how to check if letter is in a word
letter = input("type a letter")
if letter in myWord:
	print("letter is in the word")
else:
	print("letter is not in the word")

count = 0
for l in myWord:
	if l == letter:
		print(count)
	count += 1

# how to turn a string into a list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list with_ where the letters go
guessList = []

for a in myList:
	guessList.append("_")

print(guessList)

# how to replace a specific item in the list 
# So say the user types r for a guess you would 
guessList[1] = "r"
guessList.insert(0, "h")
guessList.insert("")
print(guessList)

while misses > 7
	guess = input("Guess a letter: ")
	if guess in myWord:
		# Loop through myWord and change my guessList at the correct indexes
		print("Letter is in the word")
	else:
		misses += 1

print("Game Over")

# how to loop through a string and replace letters 
mystery = list("halloween")
guessList = list("_________")

guess = input("Guess a letter: ")
index = 0

for letter in mystery:
	if letter == guess:
		guessList[index] = guess
	index += 1

print(guessList) 
