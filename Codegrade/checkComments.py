def check_comments(inFile):
    for filename in inFile:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith('def ') and (i == 0 or not lines[i-1].startswith('#')):
                    missingLine = (line.split()[1]).strip(":")
                    print(f"File: {filename} contains a function [{missingLine}]", end="")
                    print(f" on line [{i+1}] without a preceding comment.")


if __name__ == "__main__":
    try:
        inFile = input("Files to check: ").split(sep=", ")
        check_comments(inFile)
    except FileNotFoundError:
        print("Error reading file,", inFile)