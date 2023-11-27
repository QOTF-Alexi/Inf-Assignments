def problematicProgram(data):
    print("Dit programma verwacht een getal om te evalueren. Hieronder de uitkomst:")
    try:
        # Zet de data om naar int.
        if int(data) == 69:
            print("Nice")
        else:
            print("Not nice")
    except ValueError:
        # Print wanneer data niet kan worden omgezet in int.
        print("Enkel gehele getallen dienen te worden ingevoerd.\n")


def ownError(data: list):
    print("Dit programma verwacht twee getallen tussen 0 en 100, aangeleverd in een lijst:")
    try:
        if 0 < data[0] < 100 and 0 < data[1] < 100:
            print("Je hebt je aan de regels gehouden!")
        else:
            # geef een foutmelding via het uitzonderingen systeem.
            raise AttributeError
    except AttributeError:
        print("Je hebt de regels niet gevolgd!")


if __name__ == "__main__":
    problematicProgram("test")
    ownError([102, 12])