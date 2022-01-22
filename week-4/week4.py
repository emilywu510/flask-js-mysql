from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app=Flask(
    __name__,
)

app.secret_key="secret" #設定session密鑰

@app.route("/")
def home(): 
    return render_template("homepage.html")


@app.route("/member/")
def success():
    if "account_number_input" in session:
        account_number_input = session["account_number_input"]
        return render_template("success.html")
    else:
        return redirect("/")
    
@app.route("/signout")
def signout():
    session.pop("account_number_input", None)
    return redirect("/")


@app.route("/error/")
def fail():
    fail_word=request.args.get("message")
    return fail_word

@app.route("/signin", methods=["POST"])
def sign_in():
    account_number_input = request.form["account_number"]
    password_input = request.form["password"]
    if account_number_input == "test" and password_input== "test":
        session["account_number_input"] = account_number_input
        return redirect("/member/")
    elif account_number_input == "" or password_input== "":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤") 
    

app.run(port=3000)