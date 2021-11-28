class Beverage:
    def __init__(self):
        self.cost = None

    def costMethod(self):
        return self.cost


class Coffee(Beverage):
    def __init__(self):
        self.cost = 5

    def costMethod(self):
        return self.cost


class AddOnDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage
        self.cost = None

    def cost(self):
        return self.cost


class Milk(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 2

    def costMethod(self):
        return self.beverage.costMethod() + self.cost


class Cream(AddOnDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.cost = 3

    def costMethod(self):
        return self.beverage.costMethod() + self.cost


if __name__ == '__main__':
    # Coffee with Cream and Milk
    coffeeWithCreamAndMilk = Cream(Milk(Coffee()))
    print(coffeeWithCreamAndMilk.costMethod())
