import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

import re

def validate(ip):
    regex = (
        r'^(25[0-5]|'      # 250-255
        r'2[0-4][0-9]|'    # 200-249
        r'1[0-9]{2}|'      # 100-199
        r'[1-9]?[0-9])'    # 0-99 without leading zero
        r'(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'
    )
    return bool(re.match(regex, ip))


if __name__ == "__main__":
    main()
