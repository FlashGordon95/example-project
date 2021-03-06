# Author: Ian McLoughlin
# Date: October 10th, 2016

# Originally adapted from:
#   http://flask.pocoo.org/

import flask as fl
app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/name", methods=["GET", "POST"])
def name():
    return "Hello " + fl.request.form["name"] + "!"

if __name__ == "__main__":
    app.run()