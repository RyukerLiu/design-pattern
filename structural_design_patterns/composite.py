class Component:
    def get_price(self):
        raise NotImplementedError


class Product(Component):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Box(Component):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def get_price(self):
        total_price = 0
        for child in self.children:
            total_price += child.get_price()

        return total_price
