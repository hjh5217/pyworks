#turtle 모듈
import turtle as t

t.shape("turtle")
t.bgcolor('black')
t.color("white")
t.speed(0)
t.shapesize(10)

for i in range(1000):
    t.circle(100)
    t.left(10)


t.mainloop()