import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if not isinstance(s, str):
        print("Input must be a string")
        sys.exit(1)
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))


if __name__ == "__main__":
    main()
