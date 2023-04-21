#random 모듈
#1~10 : random.randint(1,10)
import random
'''
num = random.randint(1,10)
print(num)

#주사위 만들기
dice = random.randint(1,6)
print(dice)

# 주사위 10번 던지기
for i in range(0,10):
    dice = random.randint(1, 6)
    print(dice)


#리스트에서 랜덤하게 값을 추출하기
과일 = ['딸기', '수박', '참외', '사과']
'''

#주사위 2개를 10번 던지기
#두 눈의 합이 7이면 "Seven Thrown" 출력, 11이면 "Eleven THrown"출력
#두 눈이 같으면 "Double Thrown" 출력

for i in range(0, 10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("Seven Thrown")
    elif dice1 + dice2 == 11:
        print("eleven Thrown")
    elif dice1 == dice2:
        print("Double Thrown")