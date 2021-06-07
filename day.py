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


def dayOfYear(year, month, day):
    day_code=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
    month_code=[1,4,4,0,2,5,0,3,6,1,4,6]
    if (int(year/100))%2==0:
        if (int(year/100))%4==0:
            j=6
        else:
            j=2
    else:
        if (int(year/100)-1)%4==0:
            j=4
        else:
            j=0
    number_of_leap_years=int((year%100)/4)
    sum=day+month_code[month-1]+j+year%100+number_of_leap_years
    return day_code[sum%7]

print(dayOfYear(2022, 1, 8))
