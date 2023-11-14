from sys import argv


file = argv[-1]


if __name__ == "__main__":
    try:
        with open(file) as data:
            lines = data.readlines()
            last_ten_lines = lines[-10:]
            for line in last_ten_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error reading file: {file}")