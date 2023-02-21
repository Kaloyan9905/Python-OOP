class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number:
            if self.index == len(self.sequence):
                self.index = 0

            to_be_returned = self.sequence[self.index]
            self.index += 1
            self.number -= 1
            return to_be_returned

        else:
            raise StopIteration()


result = sequence_repeat('abc', 10)
for item in result:
    print(item, end='')
