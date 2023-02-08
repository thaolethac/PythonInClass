def Ceasar():
    dictA = {'A':'Y', 'B' : 'Z'}
    for i in range((ord("C")), (ord("Z")+1)):
        dictA[chr(i)] = chr(i-2)
    return dictA
print(Ceasar())

def EnCode(password):
    list = ""
    for k in password:
        list += (Ceasar()[k])
    return list
print(EnCode("H"))