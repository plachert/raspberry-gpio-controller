from flask import current_app as app
from flask import render_template

@app.route("/")
def raspi():
    print("DFASFASDFASD")
    return render_template("raspi.html")