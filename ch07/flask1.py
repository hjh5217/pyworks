#flask 웹 프레임워크 사용하기
from flask import Flask

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000 /
def index():
    return "<h1>Hello~ flask</h1>"

@app.route('/login') # 127.0.0.1:5000 /
def login():
    return "<h1><b>로그인</b> 페이지입니다.</h1>"

@app.route('/board/view')
def detail():
    return "<h1>게시판 상세 페이지</h1>"

app.run()