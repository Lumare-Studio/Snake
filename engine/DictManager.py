import copy


class DictManager(object):

    def __init__(self, origin_dict: dict):
        self.origin_dict = origin_dict
        self.copy_dict = copy.deepcopy(self.origin_dict)

    def add(self, key, value):
        self.origin_dict[key] = value
        temp = copy.deepcopy(self.origin_dict)
        self.copy_dict = temp

    def remove(self, key):
        self.origin_dict.pop(key)
        temp = copy.deepcopy(self.origin_dict)
        self.copy_dict = temp