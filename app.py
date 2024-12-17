from flask import Flask, render_template, request

from extractor import extract_video_data_from_url, extract_format_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/download", methods=["POST"])
def download():
    video_url = request.form["video_url"]
    video_data = extract_video_data_from_url(video_url)
    return render_template("download.html", video_data=video_data)


if __name__ == "__main__":
    app.run(debug=True)
