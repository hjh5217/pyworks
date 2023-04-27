# f = open() -> with open()








# kbo팀 파일에 기록
try:
    team = ['키움','삼성','롯데','두산','기아','SSG','LG','NC','한화']
    with open('./output/kbo2023.txt', 'w') as f:
        for i in team:
            if i == team[-1]:
                f.write(i)
            else:
                f.write(i + ', ')
        f.close()
except:
    print("파일을 쓸 수 없습니다.")

# kbo2023.txt 읽기
try:
    with open('./output/kbo2023.txt', 'r') as f:
        team = f.read()
        print(team)
        f.close()
except FileNotFoundError as e:
    print("파일을 읽을 수 없습니다.")
    print(e)

