import resources

Class Galaxy:
    
    def __init__(self, name="Default", NG=0, load_resources=True, resource_path="data/resources"):
        self.name = name
        
        if (load_resources)
            self.resources = resources.load_resources(resource_path)
        
        # New Game Loop
        self.NG = NG
        

    def describe(self):
        result += "This Galaxy Belongs To: {}".format(self.name)
        
        return result