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

    def create_attendance_file(self, class_name):
        directories = "python/classes/"
        json_names = [f for f in os.listdir(directories) if f.endswith(".json")]
        name = ""
        length = 0
        days = 0
        sick_days = 0
        absent_days = 0
        for a in json_names:
            with open(f"{directories}{a}") as f:
                data = json.load(f)
                if data["name"] == class_name:
                    length += 1
                    name = data["students"][0]
                    if data["attendance"][0] == "P":
                        days += 1
                    if data["attendance"][0] == "S":
                        sick_days += 1
                    if data["attendance"][0] == "A":
                        absent_days += 1
        d = {"name": name, "percent": str(days / length * 100) + "%", "sick": sick_days, "absent": absent_days}
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

