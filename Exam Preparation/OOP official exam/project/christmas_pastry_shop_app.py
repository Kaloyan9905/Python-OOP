from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if any(d.name == name for d in self.delicacies):
            raise Exception(f"{name} already exists!")

        delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.BOOTH_TYPES.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        if any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_first_booth_which_is_not_reserved(number_of_people)

        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        bill = 0
        booth = self.__find_booth_by_number(booth_number)

        bill = sum(d.price for d in booth.delicacy_orders) + booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        result = f"Booth {booth_number}:\n"
        result += f"Bill: {bill:.2f}lv."
        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_first_booth_which_is_not_reserved(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                return booth
        return None

    def __find_booth_by_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        return None

    def __find_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        return None
