class Product:
    def __init__(self, name: str, amount: int, price: float):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if 10 <= amount <= 99:
            return (self.price * amount * 0.9)
        elif amount >= 100:
            return (self.price * amount * 0.8)
        else:
            return (self.price * amount)

    def make_purchase(self, amount):
        self.amount -= amount