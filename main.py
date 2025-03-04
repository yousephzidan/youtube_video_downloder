from flask import Flask
from flask import render_template
from video.videoDownloader import video_info
from video.videoDownloader import download_video 
from flask import redirect
from flask import url_for
from flask import request

app: Flask = Flask(__name__)


@app.get("/")
def index_page():
    return render_template("index.html") 

@app.post("/info")
def info():
    url = request.form.get("url") 
    return render_template("info.html", info=video_info(url)) 

@app.post("/download")
def download():
    url = request.form.get("url")
    
    download_video(url)

    return redirect(url_for(".index_page")) 

if "__main__" == __name__:
    app.run(debug=True)
