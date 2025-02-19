import os, json
class Attendance:

    def __init__(self):
        pass

    def get_attendance(self, name):
        final_data = []
        directory = "python/attendance/"
        json_names = [f for f in os.listdir(directory) if f.endswith(".json")]
        for j in json_names:
            with open(f"{directory}{j}") as json_file:
                data = json.load(json_file)
                if data["name"] == name:
                    final_data.append(data)

        return final_data