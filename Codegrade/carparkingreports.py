from datetime import datetime
import os
import sys
import csv


def reportCars():
    requirements = input("car parking machine identifier, from date, to date (date format: DD-MM-YYYY): ")
    requirementsList = requirements.split(sep=",")
    cpm = requirementsList[0]
    fromDate = requirementsList[1]
    toDate = requirementsList[2]
    fname = ".".join(requirementsList)      # Provide a base file name

    parkedHere = []

    with open("carparklog.txt", "r", encoding="utf8") as logFile:
        for record in logFile:
            recordList = record.split(sep=";")      # Separates all items in a record.
            if fromDate < recordList[0] < toDate and recordList[1] == cpm:
                pass    # IMPLEMENT

    with open(f"{fname}.car_report.csv", "a", encoding="utf8") as file:
        file.write("license_plate;check-in;check-out;parking_fee")
    pass


def reportFees():
    requirements = input("from date, to date (date format: DD-MM-YYYY): ")
    requirementsList = requirements.split(sep=",")
    fname = ".".join(requirementsList)      # Provide a base file name

    # Calculate collected fees between given dates.

    with open(f"cpms{fname}.fee_report.csv", "a", encoding="utf8") as file:
        file.write("car_parking_machine;total_parking_fee")
    pass


def main():
    running = True
    while running:
        print("[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print("[Q] Quit program")
        choice = input("What would you like to do? ").upper()
        if choice == "P":
            reportCars()
        elif choice == "F":
            reportFees()
        elif choice == "Q":
            running = False
        else:
            print("That is not a valid option!")


if __name__ == "__main__":
    main()