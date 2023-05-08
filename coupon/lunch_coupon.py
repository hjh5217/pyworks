# 쿠폰 추첨기 만들기
import tkinter
from tkinter import *
import random

namelist = ['이진성','노승우','박성호','권지혜','김은효',
            '이경철','성의석','이유진','유성길','한주훈',
            '강정현','김현우','이영준','안재훈','김민정',
            '유세현','윤기은','오화룡','조은별','이가은']

def click():
    winner = []
    while len(winner) < 5:
        name = random.choice(namelist)
        if name not in winner:
            winner.append(name)
    output.delete(0.0, END)

    '''    
    while len(winner) < 5:
        idx = random.randint(0,19)
        if idx not in winner:
            winner.append(idx)
    '''

    for i in winner:
        output.insert(END,i+" ")

    ''' while로 안해서 실패함
    lottoList = []
    output.delete(0.0,END)
    for i in range(0,5):
        lotto = random.randrange(0, len(namelist))
        lottoList.append(namelist[lotto])
        for j in range(i):
            if lottoList[j] == lottoList[i]:
                i = i-1
        output.insert(END, lottoList[i] + " ")
    '''

window = Tk()
window.title("쿠폰 추첨기")
window.option_add('*Font', '맑은고딕 14')

#이미지 넣기
img = PhotoImage(file='bronx.png')

lbl_img = Label(window)
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0)

# 추첨 버튼
Button(window, text='추첨', command=click).grid(row=1,column=0,sticky=E)

# 이름 출력
output = Text(window, width=33, height=4, bg='yellow')
output.grid(row=2,column=0, sticky=W)

window.mainloop()