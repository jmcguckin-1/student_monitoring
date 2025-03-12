import json
import os
from Grades import *

class Classes:
    def __init__(self):
        pass

    def get_class_names(self):
        d = []
        directories = "python/classes/templates/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        for a in json_names:
            with open(f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] not in d:
                    d.append(data['name'])
        return d


    def get_class(self,name):
        d = []
        directories = "python/classes/templates/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        for a in json_names:
            with open (f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] == name:
                    d.append(data)
        return d


    def create_attendance_file(self, class_name, name):
        directories = "python/classes/attendance_records/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        total_days = 0
        present = 0
        sick_days = 0
        absent_days = 0
        for a in json_names:
            with open(f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] == class_name:
                    total_days += 1
                    if name in data["students"]:
                        if data["attendance"][name] == "P":
                            present += 1
                        if data["attendance"][name] == "S":
                            sick_days += 1
                        if data["attendance"][name] == "A":
                            absent_days += 1
        attendance_percent = str(present / total_days * 100)
        if attendance_percent == "100.0":
            g = Grades()
            g.update_behaviour_file(name, class_name, "G", f"Full Attendance in {class_name} classes so far")
        d = {"name": name, "percent": attendance_percent + "%", "class_name": class_name, "sick": sick_days, "absent": absent_days, "days": total_days}
        f1 = open(f"python/attendance/{name}_{class_name}_attendance.json", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()


    def create_class_attendance(self, attendance, name, date):
        # create a new file for this date.
        student_list = []
        directory = "python/classes/attendance_records/"
        template_dir = "python/classes/templates/"
        with open(f"{template_dir}{name}_template.json") as f:
            data = json.load(f)
            student_list = data["students"]

        d = {"name": name, "attendance": attendance, "date": date, "students": student_list}
        f1 = open(f"{directory}{name}_{date}.json", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()


    def get_assignment_names(self, class_name):
        directories = "python/assignments/assignment_names/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        return_data = []
        for b in json_names:
            with open(f"{directories}{b}") as f:
                data = json.load(f)
                if data["class_name"] == class_name:
                    return_data.append(data['assignments'])
        return return_data