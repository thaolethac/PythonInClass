import math


def SolvePtBac1(m, n):
    if m == 0:
        if (n == 0):
            return None
        else:
            return []
    else:
        return [-n/m]

# print(SolvePtBac1(3,5))


def SolvePtBac2(a, b, c):
    denta = b**2 - 4*a*c
    if (a == 0):
        return SolvePtBac1(b, c)
    else:
        if (denta == 0):
            x = -b/(2*a)
            return [x]
        elif (denta < 0):
            return []
        else:
            x1 = (-b + math.sqrt(denta))/(2*a)
            x2 = (-b - math.sqrt(denta))/(2*a)
            if (x1 <= x2):
                return [x1, x2]
            else:
                return [x2, x1]
            


print(SolvePtBac2(0, 3, 2))
