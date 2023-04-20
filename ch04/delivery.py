#배송비 계산
#주문 상품 가격이 2만원 미만이면 배송비 2500원을 포함하고
#아니면 배송비를 포함하지 않는 프로그램

def get_price(price, ea):
    price = price * ea
    delivery_fee = 2500
    if price < 20000 :
        price = price + delivery_fee
        return price
    else:
        return price

order1 = get_price(15000, 2)
print(f'주문 가격은 {order1}원 입니다')
order2 = get_price(30000, 3)
print(f'주문 가격은 {order2}원 입니다.')