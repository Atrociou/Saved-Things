print("Welcome to the To Do List")
todoList = ["Homework", "Read", "Practice" ]
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")

	choice = input("Make your choice: ")
	if choice == "q":
		exit()
		break
	elif choice == "a":
		add = input("What would you like to add? ")
		todoList.append("Run")
	elif choice == "r":
		# remove an item from the list
		todoList.pop()
		print("The item has been removed. ")
	elif choice == "p":
		print(todoList)
		# print the list
	else:
		print("That is not a choice")