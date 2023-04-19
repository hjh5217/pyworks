#seats.py
#자리배치
#입장객 수, 좌석 열, 줄수
#입장객수가 열수로 나누어 떨어지는 경우, 그렇지 않은 경우

customer = int(input("입장객 수 입력 : "))
col = int(input("좌석 열 수 입력 : "))

if customer % col == 0:
    row = int(customer / col)
else:
    row = int(customer / col) + 1


for i in range(0 , row):
    for j in range(1,col+1):
        num = col*i+j
        if num > customer:
            break
        else:
            print(f'좌석{num}',end=' ')
    print()
