from flask import Flask
from flask import request
from flask import redirect
from flask import send_file
import wget
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open("pages/index.html") as f:
        page = f.read().splitlines()
    rpage = ""
    for line in page:
        rpage += line
    return rpage
@app.route("/view/<username>", methods=["GET"])
def viewskin(username):
    with open("pages/view.html") as f:
        page = f.read().splitlines()
    rpage = ""
    for line in page:
        rpage += line
    rpage = rpage.replace("$USER$", username)
    return rpage

@app.route("/load", methods=["POST"])
def loadskin():
    user = request.form["username"]
    return redirect("/view/" +user)

@app.route("/skin/<username>")
def imgskin(username):
    wget.download("http://classicube.s3.amazonaws.com/skin/" +username +".png")
    filename = username +".png"
    return send_file(filename, mimetype="image/gif")

app.run()
