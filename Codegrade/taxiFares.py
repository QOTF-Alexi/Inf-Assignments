def calculate_fare(distance):
    base_fare = 4.00
    fare_per_140m = 0.25
    distance_in_meters = distance * 1000
    fare = base_fare + (distance_in_meters / 140) * fare_per_140m
    print(round(fare, 2))


if __name__ == "__main__":      # Only runs the function if the file is accessed directly.
    distance = float(input("Distance traveled: "))
    calculate_fare(distance)