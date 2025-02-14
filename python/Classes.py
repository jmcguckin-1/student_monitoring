import json

class Classes:
    def __init__(self):
        pass

    def get_class(self,name):
        d = []
        with open ("python/classes/class1.json") as f:
            data = json.load(f)
            if data["name"] == name:
                d.append(data)
        return d

    def update_class(self,data, name):
        d = []
        with open(f"python/classes/{name}") as f:
            old_data = json.load(f)
            old_data.update({"attendance": data["attendance"]})
            d = old_data
        f1 = open("python/classes/class1.json", "w")
        f1.write(json.dumps(d, indent=4))
        f1.close()

