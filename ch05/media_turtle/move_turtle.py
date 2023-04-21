#turtle 모듈
import turtle as t

t.shape("turtle")
t.pensize(11)
t.color('green')
for i in range(0,4):
    t.forward(100)
    t.right(90)

# 삼각형을 그린다
t.color('blue')
for i in range(0, 3):
    t.forward(100)
    t.left(120)

t.color('red')
t.circle(50) # 반지름이 50 px 인 원



t.mainloop()