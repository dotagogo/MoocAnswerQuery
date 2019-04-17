import sys
import requests
import webbrowser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("search.html")

@app.route("/search/",methods = ["GET","POST"])
def search():
    if request.method == "POST":
        course = request.form['course']
        question = request.form['question']
        search_url = f"http://mooc.forestpolice.org/cx/0/{question}"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
        data = {
            "course":course,
            "type":0,
            "option":""
        }
        return requests.post(search_url,headers = headers,data=data).text

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:1011")
    app.run(port=1011)