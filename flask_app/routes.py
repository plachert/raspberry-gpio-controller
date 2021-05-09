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
    pin_id = int(request.args.get("pin_id"))
    state = request.args.get("state")
    if state=="true":
        pinboard.turn_on(pin_id)
    else:
        pinboard.turn_off(pin_id)
    return jsonify({pin_id: state})
