from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/season')
def get_season():
    season = '봄'
    seasonlist = ['봄','여름','가을','겨울']
    return render_template('season.html',
                           season = season,
                           seasons= seasonlist)

@app.route('/loopindex', methods = ['GET'])
def loopindex():
    items = ['a','b','c','d']
    return render_template('loopindex.html', items = items)

# 회원가입 페이지
@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == "POST":
        # 데이터 가져오기 (넘겨 받기) - name 속성
        mid = request.form['memberid']
        pwd = request.form['memberpw']
        name = request.form['name']
        gender = request.form['gender']

        return render_template('memberlist.html',
                               mid = mid, pwd = pwd, name = name, gender = gender)
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)

app.run()