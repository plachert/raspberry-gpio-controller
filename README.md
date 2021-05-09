[![Python 3.7](https://img.shields.io/badge/python-3.7.3-blue.svg)](https://www.python.org/downloads/release/python-373/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

# RaspiWebController
A simple one-page Flask application for controlling GPIO pins on RaspberryPi. It enables to change the state of each pin with toggle switches. 

## How to use
Running server on RaspberryPi:
1. Create and activate virtualenv
2. Install requirements
```shell script
pip install -r requirements.txt
```
3. Set FLASK_APP to "flask_app"
```shell script
export FLASK_APP="flask_app"
```
4. Run the server with sudo:
```shell script
sudo python wsgi.py
```

On client side:

Go to the server page: https://raspberrypi.local:5000


## Technologies used
[![RaspberryPi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)](https://www.raspberrypi.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/1.1.x/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.w3schools.com/js/)
