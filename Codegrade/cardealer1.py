class Car:
    def __init__(self, brand: str, model: str, color: str, price: float):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = ""

    def sell(__init__, sold_to):
        __init__.sold = True
        __init__.sold_to = sold_to

    def print(__init__):
        print("Brand:", __init__.brand)
        print("Model:", __init__.model)
        print("Color:", __init__.color)
        print("Price:", __init__.price)
        if __init__.sold:
            print("Sold to", __init__.sold_to)
        else:
            print("Not sold yet")


class Motorcycle:
    def __init__(self, brand: str, model: str, color: str, price: float):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = ""

    def sell(__init__, sold_to):
        __init__.sold = True
        __init__.sold_to = sold_to

    def print(__init__):
        print("Brand:", __init__.brand)
        print("Model:", __init__.model)
        print("Color:", __init__.color)
        print("Price:", __init__.price)
        if __init__.sold:
            print("Sold to", __init__.sold_to)
        else:
            print("Not sold yet")


class Customer:
    def __init__(self, name: str):
        self.name = name

    def print(__init__):
        print("Name:", __init__.name)

    def __repr__(__init__):
        return __init__.name


if __name__ == "__main__":
    foo = Car("Volkswagen", "Arteon", "Silver", 57000)
    bar = Car("Fiat", "126P", "Red", 1400)
    foobar = Car("Ford", "F150", "Blue", 100000)
    baz = Car("Peel", "P50", "Red", 10000)
    m1 = Motorcycle("Yamaha", "RD250", "Blue", 2000)
    m2 = Motorcycle("Yamaha", "XJ650", "Red", 4000)
    m3 = Motorcycle("Kawasaki", "Z900RS SE", "Black", 17000)
    fizzy = Customer("Plink")
    foobar.sell(fizzy)
    foobar.print()
    bar.print()
    m2.print()
