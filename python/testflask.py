from Classes import *
from flask import Flask, request

app = Flask(__name__)
c = Classes()

@app.route("/api/get_class")
def get_class():
    name = request.args.get("name")
    return c.get_class(name)

@app.route("/api/get_names")
def get_names():
    return c.get_class_names()

@app.route("/api/update_class", methods=['POST'])
def update_class():
    data = request.json
    c.update_class(data, "class1.json")
    return ""

if __name__ == '__main__':
    app.run()