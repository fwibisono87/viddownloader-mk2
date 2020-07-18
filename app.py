from flask import *
import wtforms
import youtube
import os

app = Flask(__name__)
vidPath = os.path.join(os.getcwd(), 'temp', 'video.mp4')
audPath = os.path.join(os.getcwd(), 'temp', 'audio.mp4')
temPath = os.path.join(os.getcwd(), 'temp', 'temp.mp4')


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/input')
def add():
    return render_template("input.html")


if __name__ == '__main__':
    app.run()
