
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route("/",methods=["Get"])
def hello():
    details =[
        {
            "name":"Haresh",
            "age":"18"
        },
        {
            "name":"maverick",
            "age":"20"
        },
        {
            "carname":"Dodge Challenger",
            "model":"Hellcat"
        }
    ]
    return render_template("btn.html")
@app.route("/form",methods=["GET"])
def form():
    return render_template("register.html")


@app.route("/submit",methods=["post"])
def submit():
    username = request.form.get("fname")
    password = request.form.get("lname")

    print(username)
    print(password)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,port=3000)