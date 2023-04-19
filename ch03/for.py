#중첩 for문.py
#5행 5열
"""
for i in range(5):
    for j in range(5):
        print('*', end='')
    print('')
"""
# * 출력
# 삼각형
"""
*
**
***
****
*****
"""

for i in range(0,5):
    for j in range(0,i+1):
        print('*', end='')
    print('')

"""
i=1,j=0

"""


for i in range(5,0,-1):
    for j in range(0,i-1,1):
        print('*', end='')
    print('')


for i in range(0,5):
    for j in range(1,6):
        print(5*i+j, end=' ') # j의 종료값
    print('')
print("="*20)
row=5
col=5
for i in range(0, row):
    for j in range(1, col+1):
        num = col*i+j
        print(num, end=' ')
    print('')

