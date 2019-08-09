class FormatData:
    def __init__(self, data, attributes_to_remove):
        self.data = data
        self.attributes = attributes_to_remove
    
    def format(self):
        for contributor in self.data:
            for attribute in self.data.keys():
                if attribute in self.attributes:
                    del contributor[attribute]
        return self.data