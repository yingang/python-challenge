import datetime

for year in range(1006, 2006, 10):
    # leap year
    if year % 4:
        continue

    dt = datetime.datetime(year, 1, 26)
    if dt.weekday() == 0:   # monday
        print(year, 1, 27)  # tomorrow
