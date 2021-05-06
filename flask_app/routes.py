from flask import current_app as app
from flask import render_template, request, jsonify
from raspi.raspi_board import PinBoard

@app.before_first_request
def startup():
    global pinboard
    pinboard = PinBoard()

@app.route("/")
def raspi():
    pins_info = pinboard.get_pins_info()
    return render_template("raspi.html", title="Raspi", pins_info=pins_info)

@app.route("/background_process", methods=["POST", "GET"])
def background_process():
    state = request.args.get("pin3")
    if state:
        pinboard.turn_on(3)
    else:
        pinboard.turn_off(3)
    board_state = pinboard.get_state()
    return jsonify({"board_state": board_state})