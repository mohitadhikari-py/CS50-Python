def main():
    amount = 50
    valid_coins = [25, 10, 5]

    while amount > 0:
        print(f"Amount Due: {amount}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        if coin in valid_coins:
            amount -= coin


    print(f"Change Owed: {abs(amount)}")

main()
