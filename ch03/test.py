name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요 : "))
weight = float(input("몸무게를 입력하세요 : "))

height = height/100

bmi = weight / (height**2)

print(f'{name}님의 bmi는 {bmi:2f}') # f스트링(string) 방식
print("%s 님의 bmi는 %.2f입니다." % (name, bmi)) # %포맷 방식

if(bmi >= 25):
    print("비만입니다")
elif(bmi > 23 and bmi < 25):
    print("과체중입니다")
elif(bmi > 18.5 and bmi < 23):
    print("정상입니다")
else:
    print("저체중입니다")
