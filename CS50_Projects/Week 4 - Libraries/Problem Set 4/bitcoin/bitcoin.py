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
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=EnterYourAPI")
    content = response.json()
    price = float(content["data"]["priceUsd"])
    amount = args*price
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()

