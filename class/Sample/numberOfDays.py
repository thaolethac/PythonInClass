def numberDaysOfMonth(n):
    if n <=7 and n % 2 != 0 and n>=1 or (n >=8 and n % 2 ==0 and n <=12) :
        return 31
    if n == 9 or n==11 or n==4 or n==6 :
        return 30
    if n == 2:
        return 28
    else:
        return None

def numberOfDays(day, month):
    dict = {}
    for i in range(1,13):
        dict[i] = numberDaysOfMonth(i)
    print(dict)
    numberday = day - 1
    numberMonth = month 
    dayofnumberMonth = 0
    for key in range(1,numberMonth) :
        dayofnumberMonth = dayofnumberMonth + dict[key]
    return numberday + dayofnumberMonth
    
print(numberOfDays(3,12))


        