from flask import Flask, render_template, json, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

con = None
cursor = None

#db 연결한당
def getCursor():
    global con, cursor
    con = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='flask-board',
        autocommit='true',
        charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)

#db 닫기
def conClose() :
    con.close()

#게시글 리스트
@app.route("/board", methods=["GET"])
def getList() :
    sql = "SELECT * FROM board order by `date` desc"
    getCursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conClose()
    return json.dumps(data)

#글보기 페이지
@app.route("/board/<idx>", methods=['GET'])
def getView(idx) :
    sql = "SELECT * FROM board where idx=%s"
    getCursor()
    cursor.execute(sql,(idx))
    data = cursor.fetchone()
    conClose()
    return json.dumps(data)

#회원가입
@app.route("/member", methods=['POST'])
def memberAdd() :
    id = request.form['id']
    pw = request.form['pw']
    name = request.form['name']
    chk = "SELECT * FROM member where id=%s"
    getCursor()
    if cursor.execute(chk,(id)) :
        conClose()
        return "false"
    else :
        sql = "INSERT INTO member SET id=%s,pw=%s,name=%s"
        cursor.execute(sql,(id,pw,name))
        conClose()
        return "true"

#로그인
@app.route("/login", methods=['POST'])
def memberLogin() :
    id = request.form['id']
    pw = request.form['pw']
    chk = "SELECT * FROM member where id=%s and pw=%s"
    getCursor()
    data = cursor.execute(chk,(id,pw))
    if data == "" :
        conClose()
        return "false"
    else :
        conClose()
        return json.dumps(data)

#글작성
@app.route("/board", methods=['POST'])
def boardAdd() :
    writer = request.form['writer']
    subject = request.form['subject']
    content = request.form['content']
    sql = "INSERT INTO board SET writer=%s,subject=%s,content=%s,date=now()"
    getCursor()
    cursor.execute(sql,(writer,subject,content))
    conClose()
    return "true"

#글수정 데이터
@app.route("/board/update/<idx>", methods=['GET'])
def boardUpdateView(idx) :
    sql = "SELECT * FROM board where idx=%s"
    getCursor()
    data = cursor.execute(sql,(idx))
    return json.dumps(data)

#글수정
@app.route("/board/update/<idx>", methods=['PUT'])
def boardUpdate(idx) :
    subject = request.form['subject']
    content = request.form['content']
    sql = "UPDATE board SET subject=%s,content=%s where idx=%s"
    getCursor()
    cursor.execute(sql,(subject,content,idx))
    conClose()
    return "true"

#글삭제
@app.route("/board/delete/<idx>", methods=['DELETE'])
def boardDelete(idx) :
    sql = "DELETE FROM board where idx=%s"
    getCursor()
    cursor.execute(sql,(idx))
    conClose()
    return "true"

if __name__ == '__main__' :
    app.run(debug=True)