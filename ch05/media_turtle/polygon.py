import turtle as t

t.shape("turtle")
'''
for i in range(3):
    t.forward(100)
    t.left(120)

# penup() - 이동하는 선의 궤적이 보이지 않게 함
t.penup()
t.forward(100)
t.pendown()

for i in range(3):
    t.backward(100)
    t.left(120)
'''
def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)

polygon(5)

t.penup()
t.forward(100)
t.pendown()

polygon2(3,100)

t.mainloop()