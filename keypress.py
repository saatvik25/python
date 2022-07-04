
#keypress event

import turtle

wn = turtle.Screen() # Get a reference to the window

wn.title("Handling keypresses!")
# Change the window title

tess = turtle.Turtle() # Create our favorite turtle

def h1():


    tess.forward(30)

def h2():

    tess.left(45)

def h3():

    tess.right(45)

def h4():

    wn.bye()
# Close down the turtle window

wn.onkey(h1, "Up")

wn.onkey(h2, "Left")

wn.onkey(h3, "Right")

wn.onkey(h4, "q")

wn.listen()

wn.mainloop()
