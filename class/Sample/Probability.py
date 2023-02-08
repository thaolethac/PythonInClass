import math


def Gcd(a, b):
    if (b == 0):
        return a
    return Gcd(b, a % b)


def Probability(n):
    dem = 0
    probability = 0
    for i in range(1, int(n+1)):
        for k in range(1, k):
            if ((Gcd(i, k) == 1) and (i != k)):
                dem = dem+1
    probability = (dem/2) / ((n*(n-1)/2))
    return probability


print(Probability(1000000))


def Xs(n):
    if (n == 1):
        return 1
    return Xs(n-1)+1/(n**2)


print(1/Xs(4))
