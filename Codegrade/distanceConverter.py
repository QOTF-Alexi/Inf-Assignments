class Converter:
    def __init__(self, length: float, unit: str):
        self.length = length
        self.unit = unit.lower()
        self.convertLen = float()

    def meters(self):
        if self.unit in {"meters", "metres"}:
            self.convertLen = self.length
        elif self.unit == "inches":
            self.convertLen = self.length * 0.0254
        elif self.unit == "feet":
            self.convertLen = self.length * 0.3048
        elif self.unit == "yards":
            self.convertLen = self.length * 0.9144
        elif self.unit == "miles":
            self.convertLen = self.length * 1609.34
        elif self.unit in {"kilometers", "kilometres"}:
            self.convertLen = self.length * 1000
        elif self.unit in {"centimeters", "centimetres"}:
            self.convertLen = self.length * 0.01
        elif self.unit in {"millimeters", "millimetres"}:
            self.convertLen = self.length * 0.001
        else:
            print("Impossible conversion!")
            self.convertLen = 0
        return self.convertLen

    def inches(self):
        self.meters()
        return self.convertLen * 39.3701

    def feet(self):
        self.meters()
        return self.convertLen * 3.28084

    def yards(self):
        self.meters()
        return self.convertLen * 1.09361

    def miles(self):
        self.meters()
        return self.convertLen * 0.000621371

    def kilometers(self):
        self.meters()
        return self.convertLen * 0.001

    def centimeters(self):
        self.meters()
        return self.convertLen * 100

    def millimeters(self):
        self.meters()
        return self.convertLen * 1000


if __name__ == "__main__":
    convert = Converter(9, 'inches')
    print(convert.feet())
    print(convert.yards())
    print(convert.miles())
    print(convert.kilometers())
    print(convert.meters())
    print(convert.centimeters())
    print(convert.millimeters())