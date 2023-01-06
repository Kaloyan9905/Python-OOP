import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    def test_cat_size_is_increased(self):
        cat = Cat('Fido')
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Fido')
        cat.eat()
        self.assertEqual(cat.fed, True)

    def test_cat_is_not_sleepy(self):
        cat = Cat('Fido')
        cat.eat()
        cat.sleep()
        self.assertEqual(cat.sleepy, False)

    def test_cat_cannot_eat_if_already_fed(self):
        cat = Cat('Fido')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed(self):
        cat = Cat('Fido')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    unittest.main()
