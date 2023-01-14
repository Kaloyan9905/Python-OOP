from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Man in black", 1997, 7.00)

    def test_init_method(self):
        self.assertEqual("Man in black", self.movie.name)
        self.assertEqual(1997, self.movie.year)
        self.assertEqual(7.00, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_method(self):
        self.assertEqual("Man in black", self.movie.name)

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_method(self):
        self.assertEqual(1997, self.movie.year)

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1730
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_method(self):
        self.movie.add_actor("Sasho")
        self.movie.add_actor("Koko")
        self.assertEqual(["Sasho", "Koko"], self.movie.actors)

        result = self.movie.add_actor("Sasho")
        self.assertEqual(f"Sasho is already added in the list of actors!", result)

    def test_gt_method(self):
        self.other = Movie("Jumanji", 2018, 8.00)
        result = self.movie.__gt__(self.other)
        self.assertEqual(f'"Jumanji" is better than "Man in black"', result)
        self.movie.rating = 9.00
        result = self.movie.__gt__(self.other)
        self.assertEqual(f'"Man in black" is better than "Jumanji"', result)

    def test_repr_method(self):
        self.movie.add_actor("Sasho")
        self.movie.add_actor("Koko")
        result = f"Name: Man in black\n" \
                 f"Year of Release: 1997\n" \
                 f"Rating: 7.00\n" \
                 f"Cast: Sasho, Koko"

        self.assertEqual(result, self.movie.__repr__())

