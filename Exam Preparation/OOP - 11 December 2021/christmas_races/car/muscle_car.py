from christmas_races.car.car import Car


class MuscleCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @staticmethod
    def min_speed():
        return 250

    @staticmethod
    def max_speed():
        return 450
