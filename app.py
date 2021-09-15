from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

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

# project work

# make an instance of a class
boggle = Boggle()
# now call a function to make board
make_board = boggle.make_board()

@app.route("/boggleboard")
def display_boggle_board():
    return render_template("boggle_board.html", display_board = make_board) 


