


#polyhon
import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
side =6
side_length = 70
side_angle = 360.0/side
for i in range(6):
  t.fd(side_length)
  t.right(side_angle)
t.mainloop()  
