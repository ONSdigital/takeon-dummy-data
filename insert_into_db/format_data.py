class FormatData:
    def __init__(self, attributes_to_remove):
        self.attributes = attributes_to_remove
        self.formatted_data = {}

    def search_dict(self, dict_to_search):
        for attribute in dict_to_search:
            if type(dict_to_search[attribute]) is not type(dict()):
                self.formatted_data[attribute] = dict_to_search[attribute]
            else:
                return self.search_dict(dict_to_search[attribute])
        return self.formatted_data
