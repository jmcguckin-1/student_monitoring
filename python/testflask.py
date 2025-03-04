from Classes import *
from flask import Flask, request
from Attendance import *
from Grades import *

app = Flask(__name__)
c = Classes()
a = Attendance()
g = Grades()
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

@app.route("/api/add_behaviour", methods=['POST'])
def add_behaviour():
    data = request.json
    a.add_behaviour(data['behaviour'], data['comments'], data['class_name'], data['date'])
    return ""

@app.route("/api/get_behaviour_file")
def get_behaviour_file():
    class_name = request.args.get("class_name")
    name = request.args.get("name")
    return a.get_b_file(class_name, name)

@app.route("/api/gen_report")
def generate_full_report():
    name = request.args.get("name")
    a.generate_full_report(name)
    return ""

@app.route("/api/get_grade")
def get_grade():
    class_name = request.args.get("class_name")
    name = request.args.get("name")
    return str(g.get_average_grade(name, class_name))

@app.route("/api/add_comment", methods=['POST'])
def add_comment():
    data = request.json
    a.store_student_class_comment(data['comment'], data['name'], data['class_name'])
    return ""

if __name__ == '__main__':
    app.run()