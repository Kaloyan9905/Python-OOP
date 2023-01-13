import unittest

from project1.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def test_init_method_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.fuel_consumption = 1.25
        self.assertEqual(v.capacity, 20.0)
        self.assertEqual(v.horse_power, 110.0)
        self.assertEqual(v.capacity, 20.0)
        self.assertEqual(v.fuel_consumption, 1.25)

    def test_drive_method_not_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.fuel_consumption = 1.25
        with self.assertRaises(Exception) as ex:
            v.drive(20)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.fuel_consumption = 1.25
        v.drive(5)
        self.assertEqual(v.fuel, 13.75)

    def test_refuel_method_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.drive(5)
        v.fuel_consumption = 1.25
        v.refuel(5)
        self.assertEqual(v.fuel, 18.75)

    def test_refuel_method_not_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.fuel_consumption = 1.25
        with self.assertRaises(Exception) as ex:
            v.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method_working(self):
        v = Vehicle(20.0, 110.0)
        v.capacity = v.fuel
        v.fuel_consumption = 1.25
        actual_result = f"The vehicle has 110.0 " \
                        f"horse power with 20.0 fuel left and 1.25 fuel consumption"

        expected_result = v.__str__()
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()

