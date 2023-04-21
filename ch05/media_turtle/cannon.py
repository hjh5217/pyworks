# 거북이 대포 게임
'''
1. 키보드 방향키로 발사 각도 조절
2. 스페이스바로 발사,
3. 화살표 모양의 포탄이 하늘로 날아감
'''
import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    # y좌표가 0보다 클 경우(거북이가 땅 위에 있는 경우)
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)

    # 거북이와 목표 지점과의 거리
    d = t.distance(target,0)
    t.write(d)
    # 성공 또는 실패를 표시할 위치
    t.sety(random.randint(10,100))
    if d < 25:
        t.color('blue')
        t.write('Good!', False, "center",("",15))
    # 목표 지점에 닿지 않았을 때
    else:
        t.color("red")
        t.write("Bad!", False, "center",("",15))
        t.color("black")
        t.goto(-200,10)
        t.setheading(ang) # 기억된 머리 각도 설정

#땅 그리기
t.goto(-300,0)
t.goto(300,0)

# 목표 지점 설정
target = random.randint(50,150) # 50~150 사이의 x좌표 한 지점
t.color('green')
t.pensize(2)
t.penup()
t.goto(target-25,1)
t.pendown()
t.goto(target+25,1)

#포탄의 처음 위치
t.color("black")
t.penup()
t.goto(-200,10)
t.setheading(20)

#거북이 대포가 동작하는데 필요한 설정
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.listen()


t.mainloop()