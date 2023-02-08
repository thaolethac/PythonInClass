def numberDaysOfMonth(n):
    if n <=7 and n % 2 != 0 and n>=1 :
        return 31
    if n >=8 and n % 2 ==0 and n <=12:
        return 30
    if n == 2:
        return 28
    else:
        return None
