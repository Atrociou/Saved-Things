# how to make a list
favMovies = ["Lego Star Wars", "Nemo", "Finding Dory"]
# print the whole list
print(favMovies)
# print individually
print(favMovies[0])
# to add you can use append or insert
# append adds to the end
favMovies.append("Kill Bill")
print(favMovies)
# insert willl put the item whereever I want
favMovies.insert(1, "Peppa Pig")
print(favMovies)
# how to remove items
# remiove by name or by index
# remove by name use remove
favMovies.remove("Kill Bill")
print(favMovies)
# favMovies.remove("Endgame")
# pop will remove the last item unless an index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1)# will remove whatever is in index
print(favMovies)

# get the length of a list
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("What is your favorite movie? ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

# loop through a list
count = 1

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie)
	count = count + 1
numList = [1, 3, 5, 7, 9, 11, 13, 15]
# challenge: Loop through the the ;ist add all the numbers together anf ptint the sum

total = 0

for number in numList:
	total = total + number

	print("The sum is " + str(total)) 

if "Lego Star Wars" in favMovies:
	favMovies.remove("Lego Star Wars")
	print("removed")
else:
	print("not in list")