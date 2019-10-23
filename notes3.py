# Conditional 
print("Welcome to Movie Box")
age = int(input("How old are you?"))
if age > 17:
	print("You can see R rated movie")
else:
	print("You can NOT see an R rated movie")
print("Have a great day!")

myNumber = 4
choice = int(input("Pick a number between 1 an 10: "))
if myNumber == choice:
	print("You guessed it!")
elif choice < myNumber:
	print("Too low")
else:
	print("Too high")

# == (equal to), <, >, <=, >=, != (not equal to)


bDay = input("Is today your birthday(yes / no): ")
if bDay == "yes":
	print("Happy Birthday")
elif (bDay == "no"):
	print("Have a nice day anyway")
else:
	print("Learn how to read directions")



