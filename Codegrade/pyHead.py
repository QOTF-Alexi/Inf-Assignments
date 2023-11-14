from sys import argv


file = argv[-1]
count = 0


if __name__ == "__main__":
    try:
        with open(file) as data:
            Lines = data.readlines()
            while count <= 10:
                for line in Lines:
                    count += 1
                    print(line)
    except FileNotFoundError:
        print(f"Error reading file: {file}")