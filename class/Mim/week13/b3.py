def found(list, a):
    k = []
    for i in range(0, len(list)):
        if a == list[i]:
            k.append(i)
    return k


def getDifferences(m, n):
    x = ""
    s1 = []
    s2 = []
    count1 = 0
    count2 = 0
    for i in range(0, len(m)):
        s1.append(int(m[i]))
        s2.append(int(n[i]))
    s = set(s1).intersection(set(s2))
    ss = list(s)
    print(ss)
    for i in ss:
        if(len(found(s1,i)) == 1 and len(found(s2,i)) == 1):
            if(found(s1,i) == found(s2,i)):
                count1 = count1 + 1
    count2 = len(ss) - count1
        
    return (count1,count2)

print(getDifferences("1234", "8241"))
