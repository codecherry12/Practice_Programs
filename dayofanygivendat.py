def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    if isYearLeap(year)==True:
        if month<8:
            if month%2!=0:
                return 31
            else:
                if month==2:
                    return 29
                else:
                    return 30
        else:
            if month%2==0:
                return 31
            else:
                return 30
    else:
        if month<8:
            if month%2!=0:
                return 31
            else:
                if month==2:
                    return 28
                else:
                    return 30
        else:
            if month%2==0:
                return 31
            else:
                return 30


def dayOfYear(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    x=(( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)
    day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    return day[x]

print(dayOfYear(8,1,2001))
