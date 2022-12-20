from restaurant.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name: str, price: float, milliliters: int):
        super().__init__(name, price, milliliters)
