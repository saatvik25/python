


 import turtle

t = turtle.Turtle()
t.speed(5)

wn = turtle.Screen()
wn.bgcolor("light green")

t.shape("turtle")


def f():
    t.fd(100)


def r():
    t.right(90)


def l():
    t.left(90)


def exit():
    wn.bye()


wn.onkey(f, "Up")
wn.onkey(r, "Right")
wn.onkey(l, "Left")
wn.onkey(exit, "q")
wn.listen()
wn.mainloop()
