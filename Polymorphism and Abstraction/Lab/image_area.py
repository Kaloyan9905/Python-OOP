class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height

    def __le__(self, other):
        return self.width * self.height <= other.width * other.height

    def __gt__(self, other):
        return self.width * self.height > other.width * other.height

    def __ge__(self, other):
        return self.width * self.height >= other.width * other.height

    def __lt__(self, other):
        return self.width * self.height < other.width * other.height


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
print(a1 <= a3)
