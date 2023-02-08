
# def tach(x):
#     list = []
#     for i in str(x):
#         list.append(i)
#     return list
def obtainDigit(n):
    list = []
    for i in range(1,n+1):
        for j in str(i):
            list.append(j)
    
    return list[n-1]
    
print(obtainDigit(15))   