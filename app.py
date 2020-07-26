from flask import *
import youtube
import os

app = Flask(__name__)
vidPath = os.path.join(os.getcwd(), 'temp', 'video.mp4')
audPath = os.path.join(os.getcwd(), 'temp', 'audio.mp4')
temPath = os.path.join(os.getcwd(), 'temp', 'temp.mp4')
export = ""


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/input')
def add():
    return render_template("input.html")


@app.route('/inres', methods=['POST'])
def inres():

    if request.method == 'POST':
        URL = request.form['URL']

        video = youtube.youtube_parse_link(URL)

        global export_path
        export_path = youtube.download_progressive(video)

        return render_template("download.html")


@app.route('/finish', methods=['POST'])
def finished():
    return send_file(export_path, as_attachment=True)


if __name__ == '__main__':
    app.run()
