def main():
    running = True
    while running:
        print("[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print("[Q] Quit program")
        choice = input("What would you like to do? ").upper()
        if choice == "P":
            pass
        elif choice == "F":
            pass
        elif choice == "Q":
            running = False
        else:
            print("That is not a valid option!")


if __name__ == "__main__":
    pass