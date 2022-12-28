from wild_farm.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = ["Meat", "Fruit", "Vegetable", "Seed"]
    WEIGHT_INCREMENTAL = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

