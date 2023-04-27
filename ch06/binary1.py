#바이너리 파일이란 화상, 음성, 이미지 등의 파일로
# 0 과 1로 이루어진 파일이다.

with open("./output/data.bin", 'wb') as f:
    text = "바람이 분다."
    f.write(text.encode())

#data.bin 읽기
with open("./output/data.bin", 'rb') as f:
    text = f.read()
    print(text)
    print(text.decode())
