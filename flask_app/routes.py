from flask import current_app as app
from flask import render_template
from raspi.raspi_board import PinBoard

@app.before_first_request
def startup():
    global pinboard
    pinboard = PinBoard()

@app.route("/")
def raspi():
    print(pinboard.get_state())
    return render_template("raspi.html")

@app.route("/background_process")
def background_process():
    pass