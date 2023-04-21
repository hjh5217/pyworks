import time
import turtle as t
import random

t.shape("turtle")
"""
t.penup()
t.goto(0,150)
time.sleep(1)
t.goto(100,150)
time.sleep(1)
t.goto(0,0)
"""

#마음대로 걷는 거북이
t.speed(1)
t.shapesize(5)
t.penup()
for x in range(100):
    ang = random.randint(1,360)
    t.setheading(ang)
    t.forward(10)

t.mainloop()