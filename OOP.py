from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike:
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.description = description
        self.cost = cost

        self.sold = False

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("You cannot update the sale price of a bike that has been sold")
        self.sale_price = new_sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost
        if new_sale_price:
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition = new_condition


if __name__ == '__main__':
    bike = Bike("Red Releigh cruiser", Condition.GOOD, 450, 50)
    print(bike.sale_price)

    bike.update_sale_price(600)
    print(bike.sale_price)

    profit = bike.sell()

    print(profit)

    print(bike.sale_price)
