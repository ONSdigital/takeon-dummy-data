
class FormatData:
    def __init__(self, attributes_to_remove):
        self.attributes = attributes_to_remove
        self.formatted_data = {}

    def search_dict(self, dict_to_search, current_att=None):
        for attribute in list(dict_to_search.keys()):
            if type(dict_to_search[attribute]) is not type(dict()) and attribute not in self.attributes and isinstance(current_att, type(None)):
                self.formatted_data[attribute] = dict_to_search[attribute]
            elif attribute in self.attributes:
                continue
            elif type(dict_to_search[attribute]) is not type(dict()) and attribute not in self.attributes and not isinstance(current_att, type(None)): 
                self.formatted_data[current_att] = {attribute: dict_to_search[attribute]}
            else:
                return self.search_dict(dict_to_search[attribute], current_att = attribute)
        print(self.formatted_data)
        return self.formatted_data


