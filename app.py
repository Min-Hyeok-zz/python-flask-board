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
    
if __name__ == '__main__' :
    app.run(debug=True)