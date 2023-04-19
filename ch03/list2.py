# 문자열 - 1차원 리스트
ss = "20230419Sunny"

year = ss[:4]
print(year)


#day = 월일
day = ss[4:8]
print(day)

weather = ss[8:]
print(weather)

ss2 = year + day + weather
print(ss2)

#문자열 관련 함수
#split()
fruit = "banana, apple, strawberry"
fruitList = fruit.split(",")

print(fruitList[0])
print(fruitList[1])
print(fruitList[2])
print(fruitList)

#replace("이전문자", "새문자")
str1 = 'Hello, World'
str1 = str1.replace('World','Korea')
print(str1)

#format()
name = "Mario"
year = "40"
str2 = "My name is {0}. I am {1} years old.".format(name, year)
str3 = "My name is %s." % 'Mario'
name = "Mario"
str4 = f"My name is {name}"
print(str2)
print(str3)
print(str4)


#split() 예제 - ':' 로 구분하고 리스트로 변경하시오
string = "a:b:c:d"

stringList = string.split(":")

print(stringList)


# 두 수를 동시에 입력 받아서 더하기
"""
n1, n2 = input("두 수 입력 : ").split()

test = int(n1) + int(n2)
print(test)
"""

#find() 문자열이 존재하는 위치 반환
text = "Hello"
print(text.find('H'))
print(text.find('ll'))
print(text.find('k'))

print(text.find('Hello'))

