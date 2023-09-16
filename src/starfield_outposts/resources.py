import json

class Resource:
    def __init__(self, name="None", reqs=[]):
        self.data = {}
        self.data["name"] = name
        self.data["requires"] = reqs
    
    def set_name(self, name: str):
        self.data["name"] = name
        
    def get_name(self):
        return self.data["name"]
    
    def add_requirement(self, req: str):
        self.data["requires"].append(req)
    
    # Alias for add_requirement
    def add_req(self, req: str):
        self.add_requirement(req)
    
    def remove_requirement(self, req:str):
        if req in self.requires:
            self.data["requires"].remove(req)
    
    # Alias for remove_requirement
    def rem_req(self, req):
        self.remove_requireqment(req)
    
    def show(self):
        print("Name: {}".format(self.data["name"]))
        if len(self.data["requires"]) > 0:
            reqs = ""
            for r in self.data["requires"]:
                reqs += r + ", "
            print("Requires: {}".format(reqs[:-2]))
    
    def save_json(self, path):
        with open(os.path.join(path, self.data["name"]+".json"), "w") as f:
            f.write(json.dumps(self.data))
    
    def load_json(self, path, name):
        with open(os.path.join(path, name+".json"), "r") as f:
            self.data = json.loads(f.read())
        
        return self
    
import os

def load_resources(path: str):
    resources = {}
    
    for file in os.listdir(path):
        r = Resource()
        r.load_json(path, file[:-5])
        
        resources[r.get_name()] = r
        print("Added '{}'".format(r.get_name()))
    
    # Convert requirements into links to objects from strings
    for r in resources.keys():
        reqs = []

        for req in resources[r].data['requires']:
            reqs.append[resources[req]]
        
        r.data['requires'] = reqs
            
    
    return resources