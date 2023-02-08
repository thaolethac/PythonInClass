def extractSum(s):
    f = open(s, "r")
    list = f.read().split(' ')
    for i in range(0,len(list)):
        list[i] = int(list[i])
    return sum(list)    
extractSum("data.txt")