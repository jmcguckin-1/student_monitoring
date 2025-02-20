from Classes import *
from flask import Flask, request
from Attendance import *

app = Flask(__name__)
c = Classes()
a = Attendance()

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
    c.update_class(data['list'], data['name'])
    return ""

@app.route("/api/get_attendance_file")
def get_file():
    name = request.args.get("name")
    class_name = request.args.get("class_name")
    return a.get_attendance(name, class_name)

@app.route("/api/add_behaviour")
def add_behaviour():
    behaviour = request.args.get("behaviour")
    comments = request.args.get("comments")
    return a.get_attendance(name, class_name)

if __name__ == '__main__':
    app.run()