class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter < self.count:
            to_be_returned = self.current_number
            self.current_number += self.step
            self.counter += 1
            return to_be_returned
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
