from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("index.html", current_year=current_year)


@app.route("/start")
def get_start_page():
    return render_template("start.html")


@app.route("/user/<username>")
def user(username):
    return (f'<h1 style="text-align: center"> Hi  {username}!</h1>')


@app.route("/start/backUp")
def get_backup_page():
    return render_template("backUp.html")


@app.route("/start/miracle")
def get_miracle_page():
    return render_template("miracle.html")


if __name__ == "__main__":
    app.run(debug=True)
