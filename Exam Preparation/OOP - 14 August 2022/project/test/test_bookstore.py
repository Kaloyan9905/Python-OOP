from project.bookstore import Bookstore
import unittest


class BookStoreTest(unittest.TestCase):
    def test_init_method_working(self):
        bookstore = Bookstore(20)
        self.assertEqual(bookstore.books_limit, 20)
        self.assertEqual(bookstore.total_sold_books, 0)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {})

    def test_init_method_not_working(self):
        bookstore = Bookstore(20)

        with self.assertRaises(ValueError) as ex:
            bookstore.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid", str(ex.exception))

    def test_len_method_working(self):
        bookstore = Bookstore(20)
        bookstore.receive_book("Thor", 1)
        self.assertEqual(bookstore.__len__(), 1)

    def test_receive_method_not_enough_space(self):
        bookstore = Bookstore(20)
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("book", 30)
        self.assertEqual(f"Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_method_enough_space(self):
        bookstore = Bookstore(20)
        result = bookstore.receive_book("Thor", 1)
        self.assertEqual(f"1 copies of Thor are available in the bookstore.", result)
        self.assertEqual(bookstore.__len__(), 1)

    def test_sell_method_not_available(self):
        bookstore = Bookstore(20)
        bookstore.receive_book("Thor", 1)
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Thor1", 10)
        self.assertEqual(f"Book Thor1 doesn't exist!", str(ex.exception))

    def test_sell_method_not_enough_copies(self):
        bookstore = Bookstore(20)
        bookstore.receive_book("Thor", 1)
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Thor", 10)
        self.assertEqual(f"Thor has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_method_working(self):
        bookstore = Bookstore(25)
        bookstore.receive_book("Thor", 1)
        bookstore.receive_book("Odin", 10)
        result = bookstore.sell_book("Thor", 1)
        self.assertEqual(f"Sold 1 copies of Thor", result)
        self.assertEqual(bookstore.availability_in_store_by_book_titles["Odin"], 10)
        self.assertEqual(bookstore.total_sold_books, 1)
        self.assertEqual(bookstore.__len__(), 10)

    def test_str_method_working(self):
        bookstore = Bookstore(25)
        bookstore.receive_book("Book1", 11)
        bookstore.receive_book("Book2", 12)
        bookstore.sell_book("Book1", 10)

        result = [f"Total sold books: 10"]
        result.append(f'Current availability: 13')
        result.append(f" - Book1: 1 copies")
        result.append(f" - Book2: 12 copies")
        self.assertEqual(bookstore.__str__(), "\n".join(result))
        self.assertEqual(bookstore.__len__(), 13)


if __name__ == '__main__':
    unittest.main()
