from Classes import *
from flask import Flask, request

app = Flask(__name__)
c = Classes()

# @app.route('/')
# def method():
#     return "Yo!"

@app.route("/api/get_class")
def get_class():
    name = request.args.get("name")
    return c.getClass(name)

if __name__ == '__main__':
    app.run()