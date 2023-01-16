import unittest

from project.team import Team


class TeamTest(unittest.TestCase):
    def test_init_working(self):
        team = Team('test')
        self.assertEqual(team.name, 'test')
        self.assertEqual(team.members, {})

    def test_init_not_working(self):
        with self.assertRaises(ValueError) as ex:
            Team('test1')
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_working(self):
        team = Team('test')
        res = team.add_member(Meli=16, Aleks=17)
        correct_res = f"Successfully added: Meli, Aleks"
        self.assertEqual(team.members, {'Meli': 16, 'Aleks': 17})
        self.assertEqual(res, correct_res)

    def test_remove_member(self):
        team = Team('test')
        team.add_member(Meli=16, Aleks=17)
        res = team.remove_member("Meli")
        self.assertEqual(team.members, {"Aleks": 17})
        self.assertEqual(res, f"Member Meli removed")
        res = team.remove_member("Bobo")
        self.assertEqual(f"Member with name Bobo does not exist", res)

    def test_gt_method(self):
        team = Team('test')
        team.add_member(Meli=16, Aleks=17)
        other = Team('other')
        other.add_member(Koko=26, Bobo=11)
        res = team > other
        self.assertEqual(False, res)
        team.remove_member("Meli")
        res2 = other > team
        self.assertEqual(True, res2)

    def test_len_method_working(self):
        team = Team('test')
        team.add_member(Meli=16, Aleks=17)
        self.assertEqual(2, len(team))

    def test_add_method_working(self):
        team = Team('test')
        other = Team('other')
        team.add_member(Meli=16, Aleks=17)
        other.add_member(Koko=26, Bobo=11)
        new_team = team.__add__(other)
        res1 = {"Meli": 16, "Aleks": 17, "Koko": 26, "Bobo": 11}

        self.assertEqual(new_team.name, "testother")
        self.assertEqual(new_team.members, res1)

    def test_str_method(self):
        team = Team('test')
        team.add_member(Meli=16, Aleks=17, Koko=72)
        result = f"Team name: test\n"
        result += f"Member: Koko - 72-years old\n"
        result += f"Member: Aleks - 17-years old\n"
        result += f"Member: Meli - 16-years old"
        self.assertEqual(team.__str__(), result)
