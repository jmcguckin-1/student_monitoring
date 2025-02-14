import json

class Classes:
    def __init__(self):
        pass

    def getClass(self,name):
        d = []
        with open ("python/classes/class1.json") as f:
            data = json.load(f)
            if data["name"] == name:
                d.append(data)
        return d


