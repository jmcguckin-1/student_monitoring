import os, json
from Classes import *
class Attendance:

    def __init__(self):
        pass

    def get_attendance(self, name, class_name):
        final_data = []
        directory = "python/attendance/"
        c = Classes()
        c.create_attendance_file(class_name, name)
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                data = json.load(json_file)
                if data["class_name"] == class_name:
                    if data["name"] == name:
                        final_data.append(data)

        return final_data


    def add_behaviour(self, behaviour, comments, class_name, date):
        directory = "python/classes/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        d = []
        file = ""
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                data = json.load(json_file)
                if data["name"] == class_name and data["date"] == date:
                        data["behaviour"] = behaviour
                        file = j
                        data["comments"] = comments
                        d = data
        f1 = open(f"{directory}{file}", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()


