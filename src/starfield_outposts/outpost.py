Class Outpost:
    
    def __init__(self, name="None", resources=[], planet="None", imports=[], exports=[]):
        self.name = name
        self.resources = resources
        self.planet = planet
        self.imports = imports
        self.exports = exports

    def describe(self):
        result = ""
        result += "Outpost Name: {}\n".format(self.name)
        
        avails = ""
        for r in self.resources():
            avails += "{}, ".format(r.get_name())
        
        for i in imports:
            avails += "{}*,".format(i.get_resource().get_name())
        
        if len(avails) > 3:
            result += "Available Resources: {}".format(avails[:-3])
        
        return result
    
    def show(self):
        print(self.describe())
    
    def add_resource(self, resource):
        self.resources.append(resource)
    
    def remove_resource(self, resource):
        self.resources.remove(resource)
    
    def add_export(self, destination, resource):
        if resource not in self.resources:
            print("Error: Resource not available at this outpost.")
        
        link = Link(self, destination, resource)
        self.exports.append(link)
        destination.add_import(link)

    def add_import(self, destination, resource):
        link = Link(destination, self, resource)
        self.imports.append(link)
        destination.add_export(link)
        
        
Class Link:
    def __init__(self, origin, destination, resource):
        self.origin = origin
        self.destination = destination
        self.resource = resource
        
    def get_origin(self):
        return self.origin
    
    def get_destination(self):
        return self.destination
    
    def get_resource(self):
        return self.resource