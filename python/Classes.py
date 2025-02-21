import json
import os


class Classes:
    def __init__(self):
        pass

    def get_class_names(self):
        d = []
        directories = "python/classes/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        for a in json_names:
            with open(f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] not in d:
                    d.append(data['name'])
        return d

    def get_class(self,name):
        d = []
        directories = "python/classes/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        for a in json_names:
            with open (f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] == name:
                    d.append(data)
        return d

    def create_attendance_file(self, class_name, name):
        directories = "python/classes/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        length = 0
        days = 0
        sick_days = 0
        absent_days = 0
        for a in json_names:
            with open(f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] == class_name:
                    length += 1
                    if name in data["students"]:
                        if data["attendance"][name] == "P":
                            days += 1
                        if data["attendance"][name] == "S":
                            sick_days += 1
                        if data["attendance"][name] == "A":
                            absent_days += 1
        d = {"name": name, "percent": str(days / length * 100) + "%", "class_name": class_name, "sick": sick_days, "absent": absent_days}
        f1 = open(f"python/attendance/{name}_{class_name}_attendance.json", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()


    def update_class(self, attendance, name):
        d = []
        directories = "python/classes/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        file = ""
        for b in json_names:
             with open(f"{directories}{b}") as f:
                old_data = json.load(f)
                if old_data["name"] == name:
                    old_data.update({"attendance": attendance})
                    d = old_data
                    file = b
        f1 = open(f"{directories}{file}", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()

