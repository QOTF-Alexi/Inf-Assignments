class Product:
    def __init__(self, name: str, amount: int, price: float):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(__init__, amount):
        if 10 <= amount <= 99:
            return (__init__.price * amount * 0.9)
        elif amount >= 100:
            return (__init__.price * amount * 0.8)
        else:
            return (__init__.price * amount)

    def make_purchase(__init__, amount):
        __init__.amount -= amount