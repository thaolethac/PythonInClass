def factorial(x):
    if(x == 0):
        return 1
    return x * factorial(x-1)

def nCr(n,r):
    k = factorial(n) / (factorial(r) * factorial(n-r))
    return int(k)

print(nCr(0,0))