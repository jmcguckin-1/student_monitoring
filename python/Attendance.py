import os, json
from Classes import *
from Grades import *
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

    def get_overall_attendance(self, name):
        directory = "python/attendance/"
        final_data = []
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                data = json.load(json_file)
                if data["name"] == name:
                    current_sick = data['sick']
                    current_absent = data['absent']
                    if current_sick == 0 and current_absent == 0:
                        final_data.append(100)
                    else:
                        days = data['days']
                        attended = days
                        attended -= current_sick
                        attended -= current_absent
                        final_data.append((attended / days) * 100)
        return sum(final_data) / len(final_data)


    def add_behaviour(self, behaviour, comments, class_name, date):
        directory = "python/classes/attendance_records/"
        c = Classes()
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


    def get_student_status(self, m, c, sv):
        statuses = ["nothing to worry about", "student needs to improve their behaviour", "expulsion is a real possibility. this student has shown consistent bad behaviour with no sign of stopping"]
        if sv >=2:
            return statuses[2]
        if c >= 3 or m > 3:
            return statuses[1]
        return statuses[0]


    def create_behaviour_file(self, name, class_name):
        directory = "python/classes/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        minor_count = 0
        severe_count = 0
        concerning_count = 0
        comments = []
        for a in json_names:
            with open(f"{directory}{a}") as json_file:
                data = json.load(json_file)
                if data["name"] == class_name and name in data["students"]:
                    code = data["behaviour"][name]
                    comments.append(data["comments"][name])
                    if code == "M":
                        minor_count += 1
                    elif code == "SV":
                        severe_count += 1
                    else:
                        concerning_count += 1
        new_file_data = {"name": name, "class_name": class_name,"minor_count": minor_count, "severe_count": severe_count, "concerning_count": concerning_count, "comments": comments,
                         "status": self.get_student_status(minor_count, concerning_count, severe_count)}
        f1 = open(f"python/behaviour/{name}_{class_name}_behaviour.json", "w")
        f1.write(json.dumps(new_file_data, indent=4))
        f1.close()


    def get_b_file(self, class_name, name):
        directory = "python/behaviour/"
        return_data = []
        with open(f"{directory}{name}_{class_name}_behaviour.json") as json_file:
            data = json.load(json_file)
            return_data.append(data)

        if not return_data:
            self.create_behaviour_file(name, class_name)
            with open(f"{directory}{name}_{class_name}_behaviour.json") as json_file:
                data = json.load(json_file)
                return_data.append(data)

        return return_data


    def store_student_class_comment(self, comment, student, class_name):
        directory = "python/comments/"
        d = {"comment": comment, "student": student, "class_name": class_name}
        f1 = open(f"{directory}{student}_{class_name}_comments.json", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()


    def get_student_comments(self, student):
        directory = "python/comments/"
        return_data = []
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for a in json_names:
            with open(f"{directory}{a}") as json_file:
                data = json.load(json_file)
                if student == data["student"]:
                    return_data.append(data['comment'])
        return return_data

    def get_student_reward_eligibility(self, student):
        return_data = []
        directory = "python/behaviour/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for a in json_names:
            with open(f"{directory}{a}") as json_file:
                data = json.load(json_file)
                if student == data["name"]:
                    return_data.append(data['reward'])
        return return_data

    def generate_full_report(self, student_name):
        directory = "python/reports/"
        g = Grades()
        grades = g.get_student_grades(student_name)
        comments = self.get_student_comments(student_name)
        overall_attendance = self.get_overall_attendance(student_name)
        reward = self.get_student_reward_eligibility(student_name)
        data = [{"student_name": student_name, "attendance": overall_attendance, "reward": reward}]
        for i in range(0, len(grades)):
            d = {"grade": grades[i], "comments": comments[i]}
            data.append(d)

        f1 = open(f"{directory}{student_name}_report.json", "w")
        f1.write(json.dumps(data, indent=4))
        f1.close()

    def get_report(self, student_name):
        directory = "python/reports/"
        return_data = []
        self.generate_full_report(student_name)
        with open(f"{directory}{student_name}_report.json") as json_file:
                data = json.load(json_file)
                return_data.append(data)
        return return_data

    def eligible_for_reward(self, student_name, class_name):
        directory = "python/behaviour/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for a in json_names:
            with open(f"{directory}{a}") as json_file:
                data = json.load(json_file)
                if data["class_name"] == class_name and data["name"] == student_name:
                    if data["good_count"] >= 10:
                        data.update({"good_count": 0})
                        data["reward"] = "Yes"
                        f1 = open(f"{directory}{student_name}_{class_name}_behaviour.json", "w")
                        f1.write(json.dumps(data, indent=4))
                        f1.close()
