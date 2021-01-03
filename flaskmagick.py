from flask import Flask, render_template
from wand.image import Image
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'


@app.route("/")
def home():
  return render_template("index.html")

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route("/s")
def reading_images():
    with Image(filename = "image") as img: 
        b = img.width
        c = img.height
        d = b + c
    return render_template("index.html", answer=output)


if __name__ == "__main__":
  app.run(debug=True)
