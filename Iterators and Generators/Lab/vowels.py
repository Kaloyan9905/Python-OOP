class vowels:
    VOWELS = ["a", "o", "u", "e", "i", "y"]

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index].lower() in self.VOWELS:
                to_be_returned = self.string[self.index]
                self.index += 1
                return to_be_returned

            self.index += 1
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
