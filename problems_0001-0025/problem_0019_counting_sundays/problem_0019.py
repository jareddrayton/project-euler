sundays = 0
start_of_year = 1
for year in range(1901, 2001):
    leap = False
    if year % 4 == 0 and not year % 100 == 0:
        leap = True
    if year % 400 == 0:
        leap = True
    print(year, leap)

    months = [31, 28 if not leap else 29, 31,
              30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in months:
        if start_of_year % 7 == 1:
            sundays += 1
        start_of_year += month
if start_of_year % 7 == 1:
    sundays += 1

print(sundays)
