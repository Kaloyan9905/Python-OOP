class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

import unittest


class CarTest(unittest.TestCase):
    def test_all_methods_working(self):
        c = Car("a", "b", 1, 4)
        self.assertEqual("a", c.make)
        self.assertEqual("b", c.model)
        self.assertEqual(1, c.fuel_consumption)
        self.assertEqual(4, c.fuel_capacity)
        self.assertEqual(0, c.fuel_amount)

    def test_all_methods_not_working(self):
        c = Car("a", "b", 1, 4)

        with self.assertRaises(Exception) as ex:
            c.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            c.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            c.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            c.fuel_capacity = -10
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_working(self):
        c = Car("a", "b", 1, 12)
        c.fuel_amount = 0
        c.refuel(10)
        self.assertEqual(10, c.fuel_amount)

    def test_refuel_method_working_with_if_statement(self):
        c = Car("a", "b", 1, 6)
        c.fuel_amount = 0
        c.refuel(10)
        self.assertEqual(6, c.fuel_amount)

    def test_refuel_method_not_working(self):
        c = Car("a", "b", 1, 6)
        c.fuel_amount = 0
        with self.assertRaises(Exception) as ex:
            c.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_method_not_working(self):
        c = Car("a", "b", 1, 4)

        with self.assertRaises(Exception) as ex:
            c.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_working(self):
        c = Car("a", "b", 1, 4)
        c.fuel_amount = 100
        c.drive(10)
        self.assertEqual(99.9, c.fuel_amount)


if __name__ == '__main__':
    unittest.main()
