from datetime import datetime
import os
import sys
import json


class CarParkingMachine:
    def __init__(self, id: str, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.id = id
        self.log = CarParkingLogger(self.id)

    def check_in(self, license_plate: str, check_in: datetime = datetime.now()):
        currently_parked = self.log.read_from_json()    # IMPLEMENT
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            self.log.check_in_logger(license_plate, check_in)
            return "License registered"
        else:
            return False

    def check_out(self, license_plate: str):
        if license_plate in self.parked_cars:
            pfee = self.get_parking_fee(license_plate)
            self.log.check_out_logger(license_plate, pfee)
            del self.parked_cars[license_plate]
            return pfee
        else:
            return f"License {license_plate} not found"

    def get_parking_fee(self, license_plate: str):
        time_delta = datetime.now() - self.parked_cars[license_plate].check_in
        delta_hours = int(-(-time_delta.total_seconds() / 3600 // 1))
        pfee = format(self.hourly_rate * delta_hours, '.2f')
        return pfee


class ParkedCar:
    def __init__(self, license_plate: str, check_in: datetime = datetime.now()):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:
    def __init__(self, id: str):
        self.id = id
        self.jsonFile = "".join(("parking-machine-", str(self.id), ".json"))

    def read_from_json(self) -> list:
        jsonData = list()
        # read file
        with open(os.path.join(sys.path[0], self.jsonFile)) as outfile:
            json_data = json.load(outfile)
            # iterate over each line in data and call the add function
            for entry in json_data:
                jsonData.append(entry)

        return jsonData

    def remove_entry_from_json_file(self, value):
        data = self.read_from_json()
        for element in data:
            if element["license_plate"] == value:
                del element
                break

        with open(self.jsonFile, 'w') as file:
            json.dump(data, file)

    def check_in_logger(self, license_plate: str, check_in: datetime = datetime.now()):
        with open("carparklog.txt", "a") as data:
            data.write(f"{check_in};cpm_name={self.id};license_plate={license_plate};action=check-in\n")

        json_dict = {
            "license_plate": str(license_plate),
            "check_in": str(check_in)
        }

        if os.path.isfile(self.jsonFile):
            jsonData = self.read_from_json()
            jsonData.append(json_dict)
            json_object = json.dumps(jsonData, indent=4)
            with open(self.jsonFile, "w") as jsonData:
                jsonData.write(json_object)
        else:
            json_object = json.dumps(json_dict, indent=4)
            with open(self.jsonFile, "w") as jsonData:
                jsonData.write(f"[{json_object}]")

    def check_out_logger(self, lic_plate: str, pfee: float, chk_out: datetime = datetime.now()):
        with open("carparklog.txt", "a") as data:
            data.write(f"{chk_out};cpm_name={self.id};license_plate={lic_plate};action=check-out;parking_fee={pfee}\n")
        self.remove_entry_from_json_file(lic_plate)

    def get_machine_fee_by_day(self, car_parking_machine_id: str, search_date: str):
        dayFee = 0
        with open("carparklog.txt") as data:
            for record in data:
                recordList = record.split(sep=";")      # Separates all items in a record.
                if recordList[0].startswith(search_date):
                    if recordList[1].endswith(car_parking_machine_id):
                        recordFee = recordList[4].split(sep="=")    # Separates the number from the descriptor.
                        dayFee += float(recordFee[1])
                    else:
                        pass
                else:
                    pass
        return dayFee

    def get_total_car_fee(self, license_plate: str):
        carFee = 0
        with open("carparklog.txt") as data:
            for record in data:
                recordList = record.split(sep=";")
                compLicense = (recordList[2].split(sep="="))[1]
                if compLicense == license_plate and recordList[1].endswith(self.id):
                    recordFee = recordList[4].split(sep="=")
                    carFee += float(recordFee[1])
                else:
                    pass
        return carFee


def main():
    pmachine = CarParkingMachine("North")
    running = True
    while running:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        option = input("What would you like to do? ").upper()
        if option == "I":
            license = input("License: ")
            checkinStat = pmachine.check_in(license)
            if checkinStat is False:
                print("Capacity reached!")
            else:
                print(checkinStat)
        elif option == "O":
            license = input("License: ")
            print(f"Parking fee: {pmachine.check_out(license)} EUR")
        else:
            running = False


if __name__ == "__main__":
    main()