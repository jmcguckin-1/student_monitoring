import json, os


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
        return sum(grades) / len(grades)


    def set_grade(self, assignment, student, class_name, grade, comment):
        directory = "python/assignments/"
        d = {"assignment": assignment, "student": student, "class_name": class_name, "grade": grade, "comment": comment}
        f = open(f"{directory}{assignment}_{student}_{class_name}.json", "w")
        f.write(json.dumps(d))
        f.close()
