#매개변수가 리스트인 함수
#리스트 복사를 함수로 이용

def get_list(a):
    a2 = []
    for i in a:
        a2.append(i)
    return a2
    
    

v = [1,2,3,4]
get_list(v)
print(get_list(v))
