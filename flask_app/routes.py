from flask import current_app as app
from flask import render_template, request, jsonify
# from raspi.raspi_board import PinBoard

class MockPinBoard:
    def get_pins_info(self):
        return {3: {"bcm_repr": "GPIO2",
                    "is_valid": True},
                4: {"bcm_repr": "GND",
                    "is_valid": False},
                5: {"bcm_repr": "GPIO3",
                    "is_valid": True}}

    def set_state(self, gpio_id, state):
        print(f"Pin {gpio_id} set to {state}")

@app.before_first_request
def startup():
    global pinboard
    pinboard = MockPinBoard()

@app.route("/")
def raspi():
    pins_info = pinboard.get_pins_info()
    return render_template("raspi.html", title="Raspi", pins_info=pins_info)

@app.route("/background_process", methods=["POST", "GET"])
def background_process():
    pin_id = request.args.get("pin_id")
    state = request.args.get("state")
    # if state:
    #     pinboard.turn_on(3)
    # else:
    #     pinboard.turn_off(3)
    # board_state = pinboard.get_state()
    pinboard.set_state(pin_id, state)
    return jsonify({"board_state": "board_state"})