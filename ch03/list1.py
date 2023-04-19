#list1.py
#리스트 생성
cart = [] #빈 리스트
cart.append('계란')
cart.append('사과')
cart.append('생수')
cart.append('콩나물')

#특정한 위치에 요소 추가
cart.insert()

#리스트의 갯수
print(len(cart))

#리스트 수정
cart[2] = '커피'

#리스트 삭제
#cart.remove('계란')
cart.pop()

cart2 = ['계란','사과','생수']

print(cart)

#전체 조회
for i in cart:
    print(i)
    
#특정한 값 조회
print(cart[-1])
