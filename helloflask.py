from flask import Flask, url_for, send_from_directory, render_template
import os


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
			    smoker=url_for("static", filename="img/300x300Brinkman.jpeg"),
			    title='Home')
			   			   
@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

