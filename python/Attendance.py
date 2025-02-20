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


    def add_behaviour(self, behaviour, comments):
        pass