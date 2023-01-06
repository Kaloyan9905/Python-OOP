import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class TestsWorker(unittest.TestCase):
    def test_worker_initialized_correctly(self):
        worker = Worker('John', 1000, 100)
        self.assertEqual(worker.name, 'John')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 100)

    def test_if_energy_is_increased_after_rest(self):
        worker = Worker('John', 1000, 100)
        worker.rest()
        self.assertEqual(worker.energy, 101)

    def test_worker_tries_to_work_with_invalid_energy(self):
        worker = Worker('John', 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        worker = Worker('Bob', 1000, -2)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_money_is_increased_after_work(self):
        worker = Worker('John', 1000, 100)
        worker.money = 0
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_if_energy_is_decreased_after_work(self):
        worker = Worker('John', 1000, 100)
        worker.work()
        self.assertEqual(worker.energy, 99)

    def test_if_get_info_works_properly(self):
        worker = Worker('John', 1000, 100)
        worker.get_info()
        expected_result = f'{worker.name} has saved {worker.money} money.'
        self.assertEqual(worker.get_info(), expected_result)


if __name__ == "__main__":
    unittest.main()
