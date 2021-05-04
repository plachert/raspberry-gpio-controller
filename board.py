import RPi.GPIO as GPIO
from subprocess import check_output
import re

def get_board_map():
    pattern = "\(\d+\) \(\d+\)"
    out = check_output(["pinout"]).decode(encoding="utf-8")
    board_map = {}
    for line in out.split("\n"):
        if re.search(pattern, line):
            splitted_line = line.strip().split()
            mapper[int(splitted_line[1][1:-1])] = splitted_line[0]
            mapper[int(splitted_line[2][1:-1])] = splitted_line[3]
    return board_map



GPIO.setmode(GPIO.BCM)

class Pin:
    def __init__(self, board_number):
        pass

if __name__ == "__main__":
    print(get_board_map())