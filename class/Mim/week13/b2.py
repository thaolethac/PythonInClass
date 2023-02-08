# s = 'bajwdw'
# for i in range(0,len(s)):
def countDifferentCharacters(s):
    x = ''
    Set = []
    for i in s :
        x = x + i
    x1 = (x.lower())
    for i in range(0,len(x1)):
        Set.append(x1[i])
    return len(set(Set))
print(countDifferentCharacters(['Kingen','Pyosik']))

