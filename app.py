from flask import Flask, render_template, session, request
from flask.json import jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

# app.config['SESSION_DIR'] = "memcached"
app.config["SECRET_KEY"] = "zyxwvu"

# app.secret_key = "something else"
debug = DebugToolbarExtension(app)
# Session(app)

""" 
@app.route("/working")
def test_flask_setup():
    return "Flask setup working properly"

# to make debugtoolbar show up in the browser window, return some html file as debugtoolbar only appears after you render html file
@app.route("/debugtoolbar")
def show_debutoolbar_in_browser():
    return render_template("debugtoolbar.html")

"""
# project work

# make an instance of a class
boggle = Boggle()

"""
@app.route("/")
def display_boggle_board():
    make_board = boggle.make_board()
    session['make_board'] = make_board
    # session['make_board'] = make_board  # this is the way
    return render_template("boggle_board.html", display_board = make_board) 

"""

@app.route("/")
def display_boggle_board():
    """ Display boggle board. """
    make_board = boggle.make_board()
    session['make_board'] = make_board
    # session['make_board'] = make_board  # this is the way
    return render_template("boggle_board.html", display_board = make_board) 


# validate the guess word
@app.route("/valid-guess-word")
def validate_word():
    """ Check if the word is valid."""
    guess_word = request.args["guess_word"]
    # put board in session
    board = session['board']
    # call a method for validating a word from Boggle class
    res = boggle.check_valid_word(board, guess_word)
    jsonify_word = jsonify({"output": res})
    return jsonify_word

# get score, update number of turns, update scores
@app.route("/score", methods=["POST"])
def show_score():
    point = request.json["point"]
    highest_point = session.get("highest_point", 0)
    number_of_turn = session.get("number_of_turn", 0)

    session['number_of_turn'] = number_of_turn + 1
    session['highest_point'] = max(point, highest_point)
    # convert it to the json and get back boolean value
    result = point > highest_point
    return jsonify(result)


# axios.get("url")

