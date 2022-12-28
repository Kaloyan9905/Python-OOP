from wild_farm.animals.animal import Mammal


class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"


class Mouse(Mammal):
    ALLOWED_FOOD = ["Fruit", "Vegetable"]
    WEIGHT_INCREMENTAL = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Cat(Mammal):
    ALLOWED_FOOD = ["Meat", "Vegetable"]
    WEIGHT_INCREMENTAL = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"
