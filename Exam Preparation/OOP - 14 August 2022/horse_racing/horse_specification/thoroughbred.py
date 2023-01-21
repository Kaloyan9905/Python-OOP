from horse_racing.horse_specification.horse import Horse


class Thoroughbred(Horse):
    SPEED = 0

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.SPEED = speed

    @staticmethod
    def max_speed():
        return 140

    def train(self):
        self.SPEED += 3
        if self.SPEED > self.max_speed():
            self.SPEED = self.max_speed()
        self.speed = self.SPEED

        return self.speed
