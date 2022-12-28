from abc import ABC, abstractmethod

from wild_farm.food import Food


class Animal(ABC):
    ALLOWED_FOOD = []
    WEIGHT_INCREMENTAL = 0

    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food_type}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREMENTAL


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, " \
               f"{self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, " \
               f"{self.living_region}, {self.food_eaten}]"
