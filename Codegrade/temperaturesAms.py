import os
import sys


monthToName = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


# Loads a text file into memory
def load_txt_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


# Determine earliest and latest year of file, assuming it is sorted
def determine_years(data):
    yearMin = data[0][2]
    yearMax = data[-1][2]
    return yearMin, yearMax


# Determine latest month of file, assuming it is sorted and only the last is incomplete
def determine_lastmonth(data):
    maxMonth = data[-1][0]
    return maxMonth


# Converts floats from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit: float):
    celsius = (float(fahrenheit) - 32) * 5 / 9
    return celsius


# Calculates the average temperature for a given month of a given year
def average_temp_per_month(month, year, temperatures: dict):
    monthList = []
    addedTemps = 0
    divider = 0
    for element in temperatures:
        if str(year) in element[2] and str(month) in element[0]:
            monthList.append(element)
            divider += 1
    for temperature in range(len(monthList)):
        addedTemps += float((monthList[temperature])[3])
    averageTempMonth = addedTemps / divider
    return averageTempMonth


# Returns average annual temperature in Fahrenheit
def average_temp_per_year(data):
    year_temperatures = {}
    for row in data:
        year = row[2]
        temperature = float(row[3])
        if year not in year_temperatures:
            year_temperatures[year] = [temperature]
        else:
            year_temperatures[year].append(temperature)
    result = [(year, round(sum(temperatures) / len(temperatures), 2))
              for year, temperatures in year_temperatures.items()]
    return result   


# Returns average annual temperature in Celsius
def average_temperature_per_year_celsius(data):
    templistC = []
    for element in data:
        year = element[0]
        tempC = fahrenheit_to_celsius(float(element[1]))
        templistC.append((year, round(tempC, 2)))
    return templistC


def warmest_coldest_year(annualTemps):
    ()


# Fetches the warmest month of an entered year
def warmestMonthOfYear(year, data):
    yearList = []
    for element in data:
        if str(year) in element[2]:
            yearList.append(element)
    month = str(monthToName[max(element[1] for element in yearList)])
    print(month)


# Fetches the coldest month of an entered year
def coldestMonthOfYear(year, data):
    yearList = []
    for element in data:
        if str(year) in element[2]:
            yearList.append(element)
    month = str(monthToName[min(element[1] for element in yearList)])
    print(month)


# Lists the average temperature of every month of every year
def listAvgTemp_perMonth_everyYear(file, yearMin, yearMax, lastMonth):
    list_year_month_avgtemp = []
    for year in range(yearMin, yearMax + 1):
        if year == yearMax:
            for month in range(1, lastMonth + 1):  # HIER DUS
                avgMonthTemp = fahrenheit_to_celsius(average_temp_per_month(month, year, file))
                list_year_month_avgtemp.append((year, {month: round(avgMonthTemp, 1)}))
        else:
            for month in range(1, 13):  # HIER DUS
                avgMonthTemp = fahrenheit_to_celsius(average_temp_per_month(month, year, file))
                list_year_month_avgtemp.append((year, {month: round(avgMonthTemp, 1)}))
    print(list_year_month_avgtemp)


def main(filename):
    file = load_txt_file(filename)
    running = True
    while running:
        print("[1] Average temperatures per year (fahrenheit)")
        print("[2] Average temperatures per year (celsius)")    # Hint: Use built-in map() function.
        print("[3] Warmest and coldest year")   # as tuple based on the average temperature
        print("[4] Warmest month of a given year")
        print("[5] Coldest month of a given year")
        print("[6] List of average temperature per every month of each year")
        print("[Q] Quit the program")
        menuChoice = str(input("What would you like to do? "))
        if menuChoice == "1":
            print(average_temp_per_year(file))
        elif menuChoice == "2":
            tempsF = average_temp_per_year(file)
            print(average_temperature_per_year_celsius(tempsF))
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
            listAvgTemp_perMonth_everyYear(file, 1995, 2020, 5)
            # Print a list of tuples where the first element of each tuple is the year and the second element of the
            # tuple is a dictionary with months as the keys and the average temprature (in Celsius)
            # of each month as the value
        elif menuChoice == "7":
            print(average_temp_per_month(1, 1996, file))
        elif menuChoice == "Q":
            running = False
        else:
            print("That is not a valid entry!")


if __name__ == "__main__":
    main("NLAMSTDM.txt")