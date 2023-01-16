from christmas_races.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @staticmethod
    def min_speed():
        return 400

    @staticmethod
    def max_speed():
        return 600
