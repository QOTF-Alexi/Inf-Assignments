print("This program calculates the number of days and months contained in an input amount of years.")
try:
    years = int(input("For how many years? "))
except ValueError:      # I am of little faith.
    print("That is not a number! Please re-run.")
months = years * 12
days = years * 365
print("Months:", months, "Days:", days)