#!/usr/bin/env python
# coding: utf-8

# ## 로또 당첨 번호 가져오기
# 

# In[16]:

'''
import requests
from bs4 import BeautifulSoup

num=1063
url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
win_result = soup.select_one('div.win_result') #태그이름,클래스이름

win_list = win_result.text.split('\n')
win_list
win_list = win_result.text.split('\n')[7:13]
win_list
print('당첨번호')
print(win_list)
bonus_num = win_result.text.split('\n')[-4]
print('보너스번호')
print(bonus_num)
'''

# # 로또 당첨 번호 앱 제작

# In[43]:


import requests
from bs4 import BeautifulSoup
from tkinter import *

def lotto_win():
    num=entry.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    win_result = soup.select_one('div.win_result') #태그이름,클래스이름

    win_list = win_result.text.split('\n')[7:13]
    bonus_num = win_result.text.split('\n')[-4]
    
    output.delete(0.0, END) # 첫행 첫 문자 위치 시작
    output.insert(END, f'당첨번호: {win_list}\n보너스번호: {bonus_num}')
    
window = Tk()
window.title("로또 당첨 확인")

Label(window, text="당첨 회차 입력: ").grid(row=0, column=0,sticky=W)
#입력상자
entry = Entry(window,bg="yellow")
entry.grid(row=1, column=0, sticky=W)
#버튼
button = Button(window, text="당첨 번호 확인", command=lotto_win)
button.grid(row=2,column=0, sticky=W)
#출력상자
output = Text(window, bg='skyblue',width=50,height=5)
output.grid(row=3, column=0, sticky=W)

window.mainloop()


# In[ ]:




