class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.author = author
        self.name = name
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
