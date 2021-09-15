from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "OH-NO-KEY"
debug = DebugToolbarExtension(app)

@app.route("/working")
def test_flask_setup():
    return "Flask setup working properly"
