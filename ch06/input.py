#입력 받아 파일 쓰기

with open("./output/input.txt", 'a') as f:
    while True:
        text = input("저장할 내용을 입력해 주세요(종료 - Z) : ")
        if text == 'z':
            break
        f.write(text)
        f.write('\n')