
while True:
    try:
        usr = input("Fraction: ")
        x,y = map(int, usr.split("/"))
        if x < 0 or y < 0:
            continue
        if x > y:
            continue
        result = (100*x)/y
        if result <= 1:
             print("E")
        elif result >= 99:
             print("F")
        else:
            print(f"{result:.0f}%")
        break
    except (ValueError, ZeroDivisionError):
        pass


