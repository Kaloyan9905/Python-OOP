from christmas_races.car.muscle_car import MuscleCar
from christmas_races.car.sports_car import SportsCar
from christmas_races.driver import Driver
from christmas_races.race import Race


class Controller:
    CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.CAR_TYPES:
            return

        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")

        car = self.CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if not car.is_taken and driver.car is not None:
            old_car = self.__find_car_by_model(driver.car)
            old_car.is_taken = False
            driver.car = car.model
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {driver.car}."

        driver.car = car.model
        car.is_taken = True
        return f"Driver {driver_name} chose the car {driver.car}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_cars = sorted(self.cars, key=lambda c: c.speed_limit, reverse=True)[:3]
        result = ""

        for car in fastest_cars:
            car_model = car.model
            driver = self.__find_driver_by_car(car_model)
            if driver in race.drivers:
                driver.number_of_wins += 1
                result += f"Driver {driver.name} wins the {race_name} race with a speed of {car.speed_limit}.\n"

        return result.strip()

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_car_by_type(self, car_type):
        self.cars.reverse()
        for car in self.cars:
            if car.__class__.__name__ == car_type and not car.is_taken:
                self.cars.reverse()
                return car
        return None

    def __find_car_by_model(self, old_model):
        for car in self.cars:
            if car.model == old_model:
                return car
        return None

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def __find_driver_by_car(self, car_name):
        for driver in self.drivers:
            if driver.car == car_name:
                return driver
        return None
