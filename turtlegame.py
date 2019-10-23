from turtle import 
myTurtle = Turtle()
screen = myTurtle.getscreen()

myTurtle.penup()
myTurtle.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/2-50)
myTurtle.hideturtle()
score = 0

def updateScore():
	myTurtle.clear()
	myTurtle.write("Score: " + str(score), False, "left", font=("Arial", 20, "normal"))

updateScore()

myScreen.mainloop()
   