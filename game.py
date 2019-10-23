import random

mysteryNumber = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Guess a number from 1 to 100"))
	score += 1 # guess = guess + 1
	if guess == mysteryNumber:
		print("Good job, you guessed it!")
		break
	elif guess > mysteryNumber:
		print("Too high, try again")
	else:
		print("Too low, try again")

	print("You tried" + str(score)+ "times")
