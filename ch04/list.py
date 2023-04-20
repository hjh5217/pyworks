# 리스트

a = [1,2,3,4]

# 리스트에 5를 추가
a.append(5)

# 5를 삭제
a.pop()

print(a)

# a 리스트의 합계와 평균
sum_v = 0
for i in a :
    sum_v += i
print(f'[a] 합계 : {sum_v}')

avg = sum_v/len(a)
print(f'[a] 평균 : {avg}')

# 내장함수
print(f'sum = {sum(a)}')
b = (1,2,3,4,)
print(sum(b))


a2 = [] # 빈 리스트 생성

# for ~ in 로 복사
for i in a:
    a2.append(i*3)
print(a2)


# a 리스트에서 홀수만 저장
a3 = []
for i in a:
    if i % 2 != 0:
        a3.append(i)

print(a3)
