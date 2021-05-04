import RPi.GPIO as GPIO
from subprocess import check_output
import re

def get_rpi_pins():
        pattern = "\(\d+\) \(\d+\)"
        out = check_output(["pinout"]).decode(encoding="utf-8")
        board_map = {}
        for line in out.split("\n"):
            if re.search(pattern, line):
                splitted_line = line.strip().split()
                board_map[int(splitted_line[1][1:-1])] = splitted_line[0]
                board_map[int(splitted_line[2][1:-1])] = splitted_line[3]
        return board_map


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class PinBoard:
    def __init__(self):
        self.pins = get_rpi_pins()
        for pin_number, pin in self.pins.items():
            if self.is_valid_gpio(pin_number):
                GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.LOW)
    
    def get_state(self):
        board_state = {}
        for pin_number, pin in self.pins.items():
            pin_state = self.is_on(pin_number)
            if pin_state is None:
                board_state[pin_number] = pin
            else:
                board_state[pin_number] = pin_state
        return board_state

    def turn_on(self, pin_number):
        if self.is_valid_gpio(pin_number):
            GPIO.output(pin_number, GPIO.HIGH)

    def turn_off(self, pin_number):
        if self.is_valid_gpio(pin_number):
            GPIO.output(pin_number, GPIO.LOW)

    def is_valid_gpio(self, pin_number):
        pin = self.pins[pin_number]
        if pin in ["GPIO0", "GPIO1"]:
            return False # EEPROM channels
        return "GPIO" in pin

    def is_on(self, pin_number):
        if self.is_valid_gpio(pin_number):
            return GPIO.input(pin_number)
        

if __name__ == "__main__":
    board = PinBoard()
    print(board.is_on(3))
    board.turn_on(3)
    print(board.is_on(3))
    board.turn_on(3)
    board.turn_on(5)
    print(board.get_state())