from horse_racing.horse_specification.horse import Horse


class Appaloosa(Horse):
    SPEED = 0

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.SPEED = speed

    @staticmethod
    def max_speed():
        return 120

    def train(self):
        self.SPEED += 2
        if self.SPEED > self.max_speed():
            self.SPEED = self.max_speed()
        self.speed = self.SPEED
