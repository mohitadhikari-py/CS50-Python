

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
        except:
            raise ValueError

        if x < 0 or y < 0 or x > y!=0:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError

        percentage = int((100*x)/y)
        return percentage


def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
         return f"F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
