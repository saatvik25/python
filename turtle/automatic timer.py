
# automatic timer
 import turtle

turtle.setup(400,500)

wn = turtle.Screen()

wn.title("Using a timer to get events!")

wn.bgcolor("black")

tess = turtle.Turtle()

tess.color("yellow")

def h1():

    tess.forward(100)

    tess.left(56)

    wn.ontimer(h1, 1)

h1()

wn.mainloop()
