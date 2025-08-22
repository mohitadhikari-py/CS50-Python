import sys
import os


def validate_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    return filename

def count_lines(filename):
    code_lines = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                stripped = line.strip()
                if stripped == "" or stripped.startswith("#") or stripped == "\n":
                    continue
                code_lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return code_lines

def main():
    filename = validate_arg()
    total_lines = count_lines(filename)
    print(total_lines)

if __name__ == "__main__":
    main()
