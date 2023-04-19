# vaccine.py

borndate = int(input("출생년도 입력 : "))

if(borndate <= 2004 and borndate >= 1958):
    print("백신 접종 대상")
    borndate = str(borndate)
    borndatelist = list(borndate)
    print(type(borndate))
    print(borndatelist)
    print(borndatelist[3])
    if(borndatelist[3] == "1" or borndatelist[3] == "6"):
        print("월요일 접종")
    elif(borndatelist[3] == "2" or borndatelist[3] == "7"):
        print("화요일 접종")
    elif(borndatelist[3] == "3" or borndatelist[3] == "8"):
        print("수요일 접종")
    elif(borndatelist[3] == "4" or borndatelist[3] == "9"):
        print("목요일 접종")
    elif(borndatelist[3] == "5" or borndatelist[3] == "0"):
        print("금요일 접종")
else:
    print("접종 대상이 아닙니다.")
