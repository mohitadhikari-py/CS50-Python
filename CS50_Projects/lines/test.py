def main():
    time = input("What time is it? ")
    current_time = convert(time)

    if 7 <= current_time <= 8:
        print("breakfast time")
    elif 12 <= current_time <= 13:
        print("lunch time")
    elif 18 <= current_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = round((minutes*100)/60)
    convert_time = float(f"{hours}.{minutes}")

    return convert_time



if __name__ == "__main__":
    main()
