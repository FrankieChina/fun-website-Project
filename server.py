from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("Home.html", current_year=current_year)


@app.route("/page_2")
def get_page_2():
    return render_template("page2.html")



@app.route("/Home/persistent")
def get_persistent_page():
    return render_template("persistent.html")

@app.route("/start/backUp")
def get_backup_page():
    return render_template("backUp.html")


@app.route("/Home/miracle")
def get_miracle_page():
    return render_template("miracle.html")


if __name__ == "__main__":
    app.run(port=80,debug=True)
