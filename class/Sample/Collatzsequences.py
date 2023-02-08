def Collatzsequences(n):
    dictA = {0: 27}
    for i in range(1, n+1):
        if(dictA[i-1] % 2 !=0):
           dictA[i] = 3*(dictA[i-1])+1
        if(dictA[i-1] % 2 == 0):
           dictA[i] = (1/2)*(dictA[i-1])
        print(dictA[i])


(Collatzsequences(30))