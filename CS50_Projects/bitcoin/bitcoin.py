import requests
import sys
import json



if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    args = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=006c6c1174df307ff4dbe53de671114d0b6b2d835e6d539e5490713d60e6b413")
    content = response.json()
    price = float(content["data"]["priceUsd"])
    amount = args*price
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()

