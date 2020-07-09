from flask import Flask, render_template, request

app = Flask(__name__)

text = ["This is the first page", "This is the second page", "This is the third page"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first_page():
    return text[0]

@app.route("/second")
def second_page():
    return text[1]

@app.route("/third")
def third_page():
    return text[2]
