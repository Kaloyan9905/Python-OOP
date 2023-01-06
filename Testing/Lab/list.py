class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTest(unittest.TestCase):
    def test_remove_index_correctly(self):
        a = IntegerList()
        a.add(1)
        a.add(2)
        res = a.remove_index(0)
        self.assertEqual(res, 1)

    def test_remove_index_and_expect_error(self):
        a = IntegerList()
        a.add(1)
        a.add(2)
        with self.assertRaises(IndexError) as ex:
            a.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_add_integer_to_list_correctly(self):
        a = IntegerList()
        res = a.add(1)
        self.assertEqual(res, [1])

    def test_add_non_integer_to_list(self):
        a = IntegerList()
        a.add(1)
        with self.assertRaises(ValueError) as ex:
            a.add("k")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_init_method_correctly(self):
        a = IntegerList(1, 2)
        self.assertEqual(a.get_data(), [1, 2])

    def test_get_method_correctly(self):
        a = IntegerList(1, 2)
        self.assertEqual(a.get(0), 1)

    def test_get_method_not_working(self):
        a = IntegerList(1, 2)
        with self.assertRaises(IndexError) as ex:
            a.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_not_working_with_index_error(self):
        a = IntegerList(1, 2)
        with self.assertRaises(IndexError) as ex:
            a.insert(3, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_not_working_with_value_error(self):
        a = IntegerList(1, 2)
        with self.assertRaises(ValueError) as ex:
            a.insert(0, "k")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method_working(self):
        a = IntegerList(1, 2)
        a.insert(0, 3)
        self.assertEqual(a.get_data(), [3, 1, 2])

    def test_get_biggest_method(self):
        a = IntegerList(1, 2)
        self.assertEqual(a.get_biggest(), 2)

    def test_get_index_method(self):
        a = IntegerList(1, 2)
        self.assertEqual(a.get_index(2), 1)


if __name__ == "__main__":
    unittest.main()


