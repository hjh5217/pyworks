# 사각형의 넓이 계산 함수
# 함수이름 - rec_area

def calc_area(under, height):
    rec_area = under * height
    return rec_area

result = calc_area(4,3)
print('사각형의 면적:', calc_area(4,3))
print(f'{result}')


#삼각형의 넓이 = 밑변x높이/2

def tri_area(u , h):
    area = (u * h) / 2
    return area

result_tri = tri_area(4,5)
print('삼각형의 면적:', tri_area(4,5))
print(f'{result_tri}')


# 정사각형의 면적
"""
size = int(input("숫자를 입력: "))
area = size*size
print(area)
"""

def calc_size(n):
    area = n*n
    return area

n = int(input("숫자를 입력하세요 : " ))
print(calc_size(n))
