# 두 수를 매개변수로 전달
# 서로 같으면 곱하고, 두 수가 서로 다르면 더하는 함수

def fn_multi(x,y):
    if x == y:
        return x*y
    else:
        return x+y
result1 = fn_multi(5,5)
result2 = fn_multi(5,10)
print(result1)
print(result2)

'''
for i in range(1,10):
    print(f'4x{i} = {4*i}')
'''

dan = int(input("단수를 입력하세요"))
def gugu(dan):
    for i in range(1, 10):
        print(f'{dan}x{i} = {dan * i}')

gugu(dan)