from datetime import datetime
import sys


class CarParkingMachine:
    def __init__(self, id: str, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.id = id
        self.log = CarParkingLogger(self.id)

    def check_in(self, license_plate: str, check_in: datetime = datetime.now()):
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

    def check_in_logger(self, license_plate: str, check_in: datetime = datetime.now()):
        with open("carparklog.txt", "a") as data:
            data.write(f"{check_in};cpm_name={self.id};license_plate={license_plate};action=check-in\n")

    def check_out_logger(self, lic_plate: str, pfee: float, chk_out: datetime = datetime.now()):
        with open("carparklog.txt", "a") as data:
            data.write(f"{chk_out};cpm_name={self.id};license_plate={lic_plate};action=check-out;parking_fee={pfee}\n")

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