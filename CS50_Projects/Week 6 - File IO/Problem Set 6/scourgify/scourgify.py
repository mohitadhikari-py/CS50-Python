import os
import sys
import csv

def validate_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.exit(f"Could not read {input_file}")

    return input_file, output_file

def convert_csv(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            with open(output_file, "w", newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({
                        "first" : first,
                        "last" : last,
                        "house" : row["house"]
                    })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

def main():
    input_file,output_file = validate_args()
    convert_csv(input_file,output_file)

if __name__ == "__main__":
    main()
