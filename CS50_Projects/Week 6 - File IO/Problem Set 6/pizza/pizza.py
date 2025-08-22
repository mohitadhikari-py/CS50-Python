import sys
import csv
import os
from tabulate import tabulate

def validate_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    return filename

def read_csv(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            headers = reader.fieldnames
    except FileNotFoundError:
        sys.exit("File does not exist")

    return data, headers

def main():
    filename = validate_args()
    data, _ = read_csv(filename)
    print(tabulate(data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()


