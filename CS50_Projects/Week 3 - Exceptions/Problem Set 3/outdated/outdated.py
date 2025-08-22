months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        #case 1 7/8/1996
        if "/" in date:
            month, day, year = map(int, date.split("/"))

            if 1<= month <=12 and 1<= day <=31:
                print(f"{year}-{month:02}-{day:02}")
                break
        elif "," in date:
            month_day, year = date.strip().split(",")
            month_name, day = month_day.strip().split(" ")
            day = int(day)
            year = int(year)
            if month_name in months and 1<= day <=31:
                month = months.index(month_name) + 1
                print(f"{year:04}-{month:02}-{day:02}")
                break

    except (ValueError, IndexError):
        pass
