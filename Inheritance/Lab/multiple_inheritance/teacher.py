from multiple_inheritance.person import Person
from multiple_inheritance.employee import Employee


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."
