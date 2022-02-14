#連接資料庫
import mysql.connector 

db = mysql.connector.connect(
    host="localhost",   # 主機名稱
    database="website", 
    user="root",        
    password="123456")  

from flask import Flask, request, render_template, redirect, session, url_for

app=Flask(
    __name__,
)

app.secret_key="secret" #設定session密鑰

#首頁
@app.route("/")
def home(): 
    return render_template("homepage.html")

#會員頁面
@app.route("/member")
def success():
    if "username_input" in session:
        return render_template("success.html", name=session["name"])
    else:
        return redirect("/")


#失敗頁面
@app.route('/error')
def fail():
    message = request.args.get("message")
    return render_template('fail.html', message=message)


#註冊
@app.route("/signup", methods=["POST"])
def register():
    name_input = request.form["name"]
    username_input = request.form["username"]
    password_input = request.form["password"]
    #操作資料庫
    cursor = db.cursor()
    cursor.execute("SELECT username FROM member WHERE username=%s", (username_input,)) #處理可持續增長資料時不會一次取出所有資料(select * from ...)
    existing_username = cursor.fetchone()
    if existing_username != None :
        return redirect ("/error?message=帳號已經被註冊")
    elif name_input =="" or username_input == "" or password_input== "":
        return redirect("/error?message=請輸入姓名、帳號、密碼")
    else:
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s,%s,%s)", (name_input, username_input, password_input))
        db.commit()
        return redirect ("/")

#登入
@app.route("/signin", methods=["POST"])
def signin():
    username_input = request.form["username"]
    password_input = request.form["password"]
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM member WHERE username=%s AND password=%s", (username_input,password_input))
    result = cursor.fetchone()
    if result == None:
        return redirect ("/error?message=帳號或密碼輸入錯誤")
    else:
        session["name"] = result[0]
        session["username_input"] = username_input
        return redirect("/member")
        
#登出
@app.route("/signout")
def signout():
    session.pop("username_input", None)
    return redirect("/")   


app.run(port=3000)
