from datetime import datetime


class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    def check_in(self, license_plate: str, check_in: datetime = datetime.now()):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            return "License registered"
        else:
            return False

    def check_out(self, license_plate: str):
        if license_plate in self.parked_cars:
            pfee = self.get_parking_fee(license_plate)
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


def main():
    pmachine = CarParkingMachine()
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