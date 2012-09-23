from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    title = {"first":"Tutorial 01","second":"Tutorial 02"}
    users = ["Angel","Kristin","Etienne"]
    return render_template("index.html",title = title,users = users)

if __name__ == "__main__":
    app.run(debug = "True")
