from datetime import datetime
import os
import sys
import csv


def write_csv_file(file_name, rowsToWrite):
    with open(os.path.join(sys.path[0], file_name), 'w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rowsToWrite)


def reportCars():
    requirements = input("car parking machine identifier, from date, to date (date format: DD-MM-YYYY): ")
    requirementsList = requirements.split(sep=",")
    cpm = "=".join(["cpm_name", requirementsList[0]])
    fromDTstr = requirementsList[1]
    toDTstr = requirementsList[2]
    fromDate = datetime.strptime(fromDTstr, '%d-%m-%Y')
    toDate = datetime.strptime(toDTstr, '%d-%m-%Y')
    fname = "_".join(["parkedcars", requirementsList[0], "from", fromDTstr, "to", toDTstr])     # Provide base file name

    parkedHere = ["license_plate;check-in;check-out;parking_fee"]

    with open(os.path.join(sys.path[0], "carparklog.txt"), "r", encoding="utf8") as logFile:
        for checkin in logFile:
            checkinList = checkin.split(sep=";")      # Separates all items in a record.
            entryTime = datetime.strptime(checkinList[0], '%d-%m-%Y %H:%M:%S')
            if checkinList[3] == "action=check-in" and fromDate <= entryTime <= toDate:
                check_in = checkinList[0]
                licensePlate = checkinList[2]

                for checkout in logFile:
                    checkoutList = checkout.split(sep=";")      # Separates all items in a record.
                    if checkoutList[3] == "action=check-out" and checkoutList[2] == licensePlate:
                        exitTime = datetime.strptime(checkoutList[0], '%d-%m-%Y %H:%M:%S')
                        if fromDate <= exitTime <= toDate and checkoutList[1] == cpm:
                            check_out = checkoutList[0]
                            lPlate = checkoutList[2].strip("license_plate=")
                            pFee = checkoutList[4].strip("parking_fee=")
                            parkedHere.append(f"{lPlate};{check_in};{check_out};{pFee}")

    write_csv_file(f"{fname}.csv", parkedHere)


def reportFees():
    requirements = input("from date, to date (date format: DD-MM-YYYY): ")
    requirementsList = requirements.split(sep=",")
    fromDTstr = requirementsList[0]
    toDTstr = requirementsList[1]
    # fromDate = datetime.strptime(fromDTstr, '%d-%m-%Y')
    # toDate = datetime.strptime(toDTstr, '%d-%m-%Y')
    fname = "_".join(["totalfee_from", fromDTstr, "to", toDTstr])     # Provide base file name

    collectedFees = ["car_parking_machine;total_parking_fee"]

    with open(os.path.join(sys.path[0], "carparklog.txt"), "r", encoding="utf8") as logFile:
        cpmList = ()
        for entry in logFile:
            entryList = entry.split(sep=";")      # Separates all items in a record.
            cpm = entryList[1]
            cpmList += tuple(cpm)

    # Calculate collected fees between given dates.

    write_csv_file(f"{fname}.csv", collectedFees)
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