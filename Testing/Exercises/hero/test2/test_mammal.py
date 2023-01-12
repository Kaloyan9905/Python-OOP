import unittest

from mammal.project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def test_init_method_working(self):
        mammal = Mammal("koki", "lion", "roar")
        self.assertEqual(mammal.name, "koki")
        self.assertEqual(mammal.type, "lion")
        self.assertEqual(mammal.sound, "roar")

    def test_make_sound_method_working(self):
        mammal = Mammal("koki", "lion", "roar")
        mammal.make_sound()
        self.assertEqual(f"{mammal.name} makes {mammal.sound}", mammal.make_sound())

    def test_get_kingdom_method_working(self):
        mammal = Mammal("koki", "lion", "roar")
        mammal.__kingdom = "animals"
        self.assertEqual(mammal.get_kingdom(), "animals")

    def test_info_method_working(self):
        mammal = Mammal("koki", "lion", "roar")
        self.assertEqual(f"{mammal.name} is of type {mammal.type}", mammal.info())


if __name__ == '__main__':
    unittest.main()





