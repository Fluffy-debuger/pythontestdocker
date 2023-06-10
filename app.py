from flask import Flask,render_template,redirect
import requests

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def login():
    return render_template("login.html")


@app.route("/home",methods=['GET','POST'])
def home():
    return "welcome"


@app.route("/signup")
def signup():
    return render_template("signup.html")


app.run(port=5000,debug=True)