class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.keys = list(dict_object.keys())
        self.values = list(dict_object.values())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key, value = self.keys[self.index], self.values[self.index]
            self.index += 1
            return key, value

        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
