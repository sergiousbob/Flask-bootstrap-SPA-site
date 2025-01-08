import os

from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, redirect, send_from_directory, send_file

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route("/")
def index():
    return render_template("index.html", h1 = "Video compression by SergiousBob")

@app.route("/about")
def get_page_about():
    return render_template("about.html", h1 = "О проекте")

# @app.route('/test', methods = ['GET', 'POST'])
# def test():
#     return redirect("https://www.google.com")

@app.route("/download")
def Download_File():
    PATH = "install/portable_compress.rar"
    return send_file(PATH, as_attachment=True)

@app.route("/download_exe")
def Download_Exe():
    PATH = "install/vid_compress_install.exe"
    return send_file(PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)