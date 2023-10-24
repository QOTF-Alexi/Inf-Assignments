import os
import sys


def load_txt_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


def fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 1.8
    return celsius


# Returns average annual temperature in Fahrenheit
def average_temp_per_year(temperatures: dict):
    yearList = []
    averageTempList = []
    for year in range(1995, 2021):
        addedTemps = 0
        for element in temperatures:
            if str(year) in element[2]:
                yearList.append(element)
        # Calculate average here
        for temperature in range(len(yearList)):
            addedTemps += float((yearList[temperature])[3])
        averageTemp = round(addedTemps / len(yearList), 1)
        averageTempList.append(tuple((str(year), averageTemp)))
    print(averageTempList)
    return averageTempList


def warmest_coldest_year(annualTemps):
    ()


def warmestMonthOfYear(year, file):
    yearList = []
    for element in file:
        if str(year) in element[2]:
            yearList.append(element)


def coldestMonthOfYear(year, file):
    yearList = []
    for element in file:
        if str(year) in element[2]:
            yearList.append(element)


def listAvgTemp_perMonth_everyYear(file):
    ()


def main(filename):
    file = load_txt_file(filename)
    running = True
    while running:
        print("[1] Average temperatures per year (fahrenheit)")
        print("[2] Average temperatures per year (celsius)")    # Hint: Use built-in map() function.
        print("[3] Warmest and coldest year")   # as tuple based on the average temperature
        print("[4] Warmest month of a year")    # based on the input year of the user (full month name)
        print("[5] Coldest month of a year")    # based on the input year of the user (full month name)
        print("[6] List of average temperature per every month of each year")
        print("[Q] Quit the program")
        menuChoice = str(input("What would you like to do? "))
        if menuChoice == "1":
            average_temp_per_year(file)
        elif menuChoice == "2":
            ()
        elif menuChoice == "3":
            annualTemps = average_temp_per_year(file)
            warmest_coldest_year(annualTemps)
        elif menuChoice == "4":
            year = input("Enter a year: ")
            warmestMonthOfYear(year, file)
        elif menuChoice == "5":
            year = input("Enter a year: ")
            coldestMonthOfYear(year, file)
        elif menuChoice == "6":
            listAvgTemp_perMonth_everyYear(file)
            # Print a list of tuples where the first element of each tuple is the year and the second element of the
            # tuple is a dictionary with months as the keys and the average temprature (in Celsius)
            # of each month as the value
        elif menuChoice == "Q":
            running = False
        else:
            print("That is not a valid entry!")


if __name__ == "__main__":
    main("NLAMSTDM.txt")