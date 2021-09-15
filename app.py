from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH-NO-KEY"
debug = DebugToolbarExtension(app)

@app.route("/working")
def test_flask_setup():
    return "Flask setup working properly"

# to make debugtoolbar show up in the browser window, return some html file as debugtoolbar only appears after you render html file
@app.route("/debugtoolbar")
def show_debutoolbar_in_browser():
    return render_template("debugtoolbar.html")
