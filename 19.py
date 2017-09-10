leap_years = [y for y in range(1901, 2000) if y % 4 == 0 or (y % 100 == 0 and y % 400 != 0)]
long_months = [0, 2, 4, 6, 7, 9, 11]

def days_in_month(month, year):
	if month == 1:
		if year in leap_years:
			return 29
		else:
			return 28
	else:
		if month in long_months:
			return 31
		else:
			return 30

count = 0
weekday = 0
for year in range(1900, 2001):
	for month in range(0, 12):
		if weekday == 6 and year > 1900:
			count += 1

		weekday += days_in_month(month, year)
		weekday %= 7

print count