from need_for_speed.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption
