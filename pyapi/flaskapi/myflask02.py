#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

@app.route("/smelly/<name>")
def smelly(name):
    return f"{name} is smelly."

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

