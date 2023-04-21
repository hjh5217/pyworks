#turtle 모듈
import turtle as t

t.shape("turtle")
t.bgcolor("yellow")
t.fillcolor("blue")
t.shapesize(3)

# 변의 갯수 n , 각 변의 길이 d , 각 변의 각도 a
n = 4
d = 100
a = 90

for i in range(n):
    t.forward(d)
    t.right(a)

n = 3
for i in range(n):
    t.forward(d)
    t.left(a)

t.mainloop()