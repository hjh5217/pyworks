import sqlite3

conn = sqlite3.connect("c:/pydb/mydb.db")

#print(conn)

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

def select():
    # 모든 조작(삽입, 검색, 수정, 삭제)을 수행하는 함수
    cursur = conn.cursor()
    sql = "SELECT * FROM employee"
    cursur.execute(sql)

    # 전체 검색 - fetchall(), 특정 1개 검색 - fetchone()
    # 자료구조가 리스트임
    rs = cursur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e103', '안산', 22, 10000)"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def update():
    conn = getconn()
    cursor = conn.cursor()
    sql = "UPDATE employee SET age = 42 WHERE name = '추신수'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE empid = 'e103'"
    cursor.execute(sql)
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 사원번호가 'e102' 인 사원 삭제
    sql = "DELETE FROM employee WHERE empid = 'e102'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

delete()
select()