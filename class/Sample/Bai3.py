def f(x): return x**2 - 3


print(f(2))


def Loop(x):
    if (x == 0):
        return 1
    return (1/2)* ((3/Loop(x-1)) + Loop(x-1)) 

def Limit(m):
    

