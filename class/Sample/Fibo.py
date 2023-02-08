def Fibonacy(n):
    if(n <=2):
        return 1
    return Fibonacy(n-1) + Fibonacy(n-2)
print(Fibonacy(1))