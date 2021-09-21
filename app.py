from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
from flask_session import Session

app = Flask(__name__)

# app.config['SESSION_DIR'] = "memcached"
app.config["SECRET_KEY"] = "zyxwvu"

# app.secret_key = "something else"
debug = DebugToolbarExtension(app)
Session(app)


@app.route("/working")
def test_flask_setup():
    return "Flask setup working properly"

# to make debugtoolbar show up in the browser window, return some html file as debugtoolbar only appears after you render html file
@app.route("/debugtoolbar")
def show_debutoolbar_in_browser():
    return render_template("debugtoolbar.html")

# project work

# make an instance of a class
boggle = Boggle()

# now call a function to make board
# make_board = boggle.make_board()
# session['boggle_board'] = make_board

@app.route("/")
def display_boggle_board():
    make_board = boggle.make_board()
    session['make_board'] = make_board
    # session['make_board'] = make_board  # this is the way
    return render_template("boggle_board.html", display_board = make_board) 


