# map(), filter()
# 리스트를 매개변수로 전달

def times3(a):
    a2 = []
    for i in a:
        a2.append(3*i)
    return a2

v = [1,2,3,4]
print(times3(v))

# lambda 함수의 map() 사용
times2 = lambda x : 3*x
# map(함수, 리스트)
# map()은 list()를 사용해서 리스트로 반환함
def times(x):
    return 3 * x
result = map(times2,v)
print(list(result))

# filter() 와 lambda 사용
# 음의 정수를 출력하시오
def negative(n):
    return n < 0
li = [-5,-1,2,-11,76]

#negative = lambda x : x < 0
value = filter(negative, li)
print(list(value))