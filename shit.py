from datetime import date
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        m = self.month
        d = self.day
        y = self.year
        return f"{d}{m}{y}"

    def __sub__(self, _date):
        d1 = date(2000 + self.year, self.month, self.day)
        d2 = date(2000 + _date.year, _date.month, _date.day)
        return abs((d2 - d1)).days

dates = []

for year in range(2024, 2100):
    for month in range(10, 13):
        for day in range(1, 10):
            dates.append(Date(day, month, year - 2000))

def isGoodDate(date):
    m = date.month
    d = date.day
    y = date.year
    return m % d == 0 and y % m == 0


filteredDates = [d for d in dates if isGoodDate(d)]

longestGap = 0
bestPair = ()
for i in range(0, len(filteredDates) - 1):
    diff = filteredDates[i] - filteredDates[i + 1]
    if diff > longestGap:
        longestGap = diff
        bestPair = (filteredDates[i], filteredDates[i + 1])

(a, b) = bestPair
print(a)
print(b)
print(longestGap)