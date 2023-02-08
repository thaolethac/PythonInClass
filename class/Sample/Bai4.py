def CheckTamgiac(a,b,c):
    if(a + b > c and a +c >b and b +c >a):
        return True
    else:
        return False

def Perimeter(n):
    dem = 0
    for i in range(1,n+1):
        for k in range(1,n+1):
            for m in range(1, n+1):
                if CheckTamgiac(i,k,m) and i + k + m == n:
                    dem = dem +1
                    return dem
                
print(Perimeter(10))
                    
            