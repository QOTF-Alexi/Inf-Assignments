meal = float(input("Cost of the meal: "))
tip = round(meal*0.15, 3)
tax = round(meal*0.21, 3)
strtax = str(tax)
strtip = str(tip)
total = str(round(meal+tip+tax, 3))
print("Tax: " + strtax + ", Tip: " + strtip, ", Total: " + total)