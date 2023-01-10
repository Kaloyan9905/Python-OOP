import unittest

from project2.hero import Hero


class HeroTest(unittest.TestCase):
    def test_init_method_working(self):
        hero = Hero("Bobec", 82, 1000.0, 567.0)
        self.assertEqual(hero.username, "Bobec")
        self.assertEqual(hero.level, 82)
        self.assertEqual(hero.health, 1000.0)
        self.assertEqual(hero.damage, 567.0)

    def test_battle_method_working(self):
        hero = Hero("Bobec", 82, 1000.0, 567.0)
        enemy_hero = Hero("Koko", 89, 1230, 321)
        hero.battle(enemy_hero)
        self.assertEqual(hero.health, -27569.0)
        self.assertEqual(enemy_hero.health, -45264.0)

    def test_battle_method_both_heroes_with_negative_health(self):
        hero = Hero("Bobec", 82, 1000.0, 567.0)
        enemy_hero = Hero("Koko", 89, 1230, 321)
        hero.battle(enemy_hero)
        self.assertEqual(hero.health, -27569.0)
        self.assertEqual(enemy_hero.health, -45264.0)

    def test_battle_method_hero_wins(self):
        hero = Hero("Bobec", 90, 10000.0, 5670.0)
        enemy_hero = Hero("Koko", 89, 1230.0, 3.0)
        result = hero.battle(enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(hero.level, 91)
        self.assertEqual(hero.health, 9738.0)
        self.assertEqual(hero.damage, 5675.0)

    def test_battle_method_draw(self):
        hero = Hero("Bobec", 90, 100.0, 56.0)
        enemy_hero = Hero("Koko", 89, 1230.0, 3.0)
        result = enemy_hero.battle(hero)
        self.assertEqual("Draw", result)

    def test_battle_method_enemy_hero_wins(self):
        hero = Hero("Bobec", 90, 10000.0, 56.0)
        enemy_hero = Hero("Koko", 89, 12000.0, 3000.0)
        result = hero.battle(enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(enemy_hero.level, 90)
        self.assertEqual(enemy_hero.health, 6965.0)
        self.assertEqual(enemy_hero.damage, 3005.0)

    def test_fight_yourself_attempt(self):
        hero = Hero("Bobec", 90, 10000.0, 5670.0)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_invalid_health_by_hero(self):
        hero = Hero("Bobec", 90, -10000.0, 5670.0)
        enemy_hero = Hero("Koko", 89, 1230.0, 3.0)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_invalid_health_by_enemy_hero(self):
        hero = Hero("Bobec", 90, 10000.0, 5670.0)
        enemy_hero = Hero("Koko", 89, -1230.0, 3.0)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_str_method_working(self):
        hero = Hero("Bobec", 90, 10000.0, 5670.0)
        result = f"Hero {hero.username}: {hero.level} lvl\n" \
                 f"Health: {hero.health}\n" \
                 f"Damage: {hero.damage}\n"

        self.assertEqual(result, hero.__str__())


if __name__ == "__main__":
    unittest.main()
