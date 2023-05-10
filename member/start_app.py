# 컨트롤러 start_app.py
# templates 폴더, static 폴더
# 웹 서버 - flask
from flask import Flask, render_template, request, \
    redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.secret_key = "asdfqqewr1234%#@"

# sqlite3와 연동 - 연결 객체 생성
def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/member.db")
    return conn
print(getconn(), "연결 객체 생성됨")

# board 테이블 연동
def create_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE board(
            bno         INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT NOT NULL,
            content     TEXT NOT NULL,
            createdate  DATETIME DEFAULT(datetime('now','localtime')),
            hit         INTEGER DEFAULT 0,
            memberid    TEXT NOT NULL,
            FOREIGN KEY(memberid) REFERENCES member(memberid) ON DELETE CASCADE
        )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성")

def insert_board():
    conn=getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO board(title,content,memberid) VALUES (?,?,?)"
    cursor.execute(sql,("안녕하세요","날씨맑음","juhoon"))
    conn.commit()
    conn.close()

def drop_board():
    conn=getconn()
    cursor = conn.cursor()
    sql = "DROP TABLE board"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def select_board():
    conn=getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    print(boardlist)
    conn.close()
select_board()
# url - '/' 경로 설정
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

# 회원 목록
@app.route('/memberlist', methods = ['GET'])
def memberlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql)  # 검색 수행
    rs = cursor.fetchall()
    conn.close()
    # db에 저장된 자료(rs)를 memberlist.html에 보내줌
    return render_template('memberlist.html', rs=rs)

# 회원 가입
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 가입 폼에 입력된 자료 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd1']
        name = request.form['name']
        gender = request.form['gender']
        #db에 저장
        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO member(memberid, passwd, name, gender) " \
              f"VALUES ('{id}', '{pw}', '{name}', '{gender}')"
        # 자동 로그인 - 세션 발급
        session['userid'] = request.form['memberid']
        cursor.execute(sql)  # 검색 수행
        conn.commit()  # 커밋 완료
        conn.close()
        # redirect - 회원가입후 회원 목록 페이지로 강제로 이동 시킴
        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')

#로그인 페이지
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        # 로그인폼에 입력된 데이터 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd']

        #database에 접속 - 로그인 체크
        conn = getconn()
        cursor = conn.cursor()
        # 동적 바인딩
        sql = f"SELECT * FROM member " \
              f"WHERE memberid = '{id}' AND passwd = '{pw}'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        print(rs)
        conn.close()

        if rs: # rs = True
            session['userid'] = rs[0]  #memberid를 세션에 저장(세션 발급)
            return redirect(url_for('index'))
        else:
            error_msg = "아이디나 비밀번호를 확인해주세요"
            return render_template('login.html', error_msg=error_msg)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()  #모든 세션 삭제
    return redirect(url_for('index'))

@app.route('/boardlist', methods = ['GET'])
def boardlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    conn.close()
    return render_template('boardlist.html', boardlist = boardlist)

#글쓰기
@app.route('/writing')
def writing():
    return render_template('writing.html')
app.run()