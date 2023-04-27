import time
# 재귀 함수
# 종료 조건을 항상 명시(if ~ else)

#1부터 5까지 곱하기
gob = 1 #곱셈에서는 1을 기억
for i in range(1, 6):
    gob = gob*i
    print(i, gob)

def getgob(n):
    gob = 1  # 곱셈에서는 1을 기억
    for i in range(1, n+1):
        gob = gob * i
    return gob

start = time.time()
print(getgob(1000))
end = time.time()
print(end-start)

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(10))

def sos(n):
    for i in range(0,n):
        print("help me!")
        #종료 조건
        if n == 1:
            return""
        else:
            return sos(n-1)
        """
        n=3, help me!, sos(2)
        n=2, help me!, sos(1)
        n=1, help me!, help me!,help me!
        """

sos(3)