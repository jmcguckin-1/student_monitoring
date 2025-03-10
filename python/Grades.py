import json, os
from Classes import *

class Grades:

    def __init__(self):
        pass


    def get_average_grade(self, student, class_name):
        directory = "python/assignments/"
        grades = []
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                json_data = json.load(json_file)
                if json_data["student"] == student and json_data["class_name"] == class_name:
                    grades.append(json_data["grade"])
        if len(grades) != 0:
            return sum(grades) / len(grades)


    def set_grade(self, assignment, student, class_name, grade, comment):
        directory = "python/assignments/"
        d = {"assignment": assignment, "student": student, "class_name": class_name, "grade": int(grade), "comment": comment}
        f = open(f"{directory}{assignment}_{student}_{class_name}.json", "w")
        f.write(json.dumps(d))
        f.close()


    def get_student_grades(self, student):
        return_data = []
        c = Classes()
        classes = c.get_class_names()
        for c in classes:
            grade = self.get_average_grade(student, c)
            if grade is not None:
                return_data.append({"class": c, "grade": grade})
        return return_data

    def has_student_submitted(self, student, assignment, class_name):
        directory = "python/submitted_assignments/"
        submitted = False
        date_submitted = ""
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                json_data = json.load(json_file)
                if json_data["name"] == student and json_data["class_name"] == class_name:
                    if json_data["assignment_name"] == assignment:
                        submitted = True
                        date_submitted = json_data["submit_date"]
        late = self.is_assignment_late(class_name, student, date_submitted)
        return {"submitted": submitted, "late": late}

    def is_assignment_late(self, class_name, assignment, submit_date):
        directory = "python/assignments/assignment_names/"
        late = False
        names = []
        dates = []
        index = 0
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                json_data = json.load(json_file)
                if json_data["class_name"] == class_name:
                    names = json_data["assignments"]
                    dates = json_data["due_date"]

        for i in range(0, len(names)):
            if assignment == names[i]:
               index = i

        if submit_date > dates[index]:
            late = True
        return late

    def update_behaviour_file(self, student, class_name, behaviour, comments):
        directory = "python/behaviour/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        d = []
        file = ""
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                json_data = json.load(json_file)
                if json_data["class_name"] == class_name and json_data["name"] == student:
                    file = j
                    if behaviour == "M":
                        json_data.update({"minor_count": json_data["minor_count"] + 1})
                    elif behaviour == "C":
                        json_data.update({"concerning_count": json_data["concerning_count"] + 1})
                    elif behaviour == "SV":
                        json_data.update({"severe_count": json_data["severe_count"] + 1})
                    else:
                        if 'good_count' in json_data:
                            json_data.update({"good_count": json_data["good_count"] + 1})
                        else:
                            json_data["good_count"] = 1
                    json_data["comments"].append(comments)
                    d = json_data
        f1 = open(f"{directory}{file}", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()

