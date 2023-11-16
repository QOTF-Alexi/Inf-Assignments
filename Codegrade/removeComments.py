from sys import argv


file = argv[-1]


def remove_comments(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f:
        for line in lines:
            if '#' in line:
                line = line[:line.index('#')]
            f.write(line)


if __name__ == "__main__":
    try:
        inFile = input("File to read: ")
        outFile = input("File to save: ")
        remove_comments(inFile, outFile)
    except FileNotFoundError:
        print("Error reading file,", inFile)