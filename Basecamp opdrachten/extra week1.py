from math import remainder #cheating
def divisions():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    a = x/y
    b = x//y
    c = remainder(x, y)
    print("Quotient:", a, "Floor:", b, "Remainder:", c)

def hmsconv():
    sec = int(input("Enter a time in seconds: "))
    min = sec//60
    hrs = sec//3600
    if sec >= 60:
        sec -= min*60
    if min >= 60:
        min -= hrs*60
    print(hrs,":",min,":",sec)

def triarea():
    base = float(input("Enter the size of the base: "))
    height = float(input("Enter the height: "))
    area = (base*height)/2
    print("The area of the triangle is:", area)

triarea()