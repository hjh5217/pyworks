# 1~100 까지의 자연수 중 배수와 그 배수의 개수를 계산하는 함수를 작성하시오
import math

def count(input):
    for i in range(1,100):
        if (input*i) > 100:
            print(f'배수의 개수 : {math.trunc(100/input)} 개')
            break
        else:
            print(input*i)

input = int(input("자연수를 입력 하시오 : "))
count(input)