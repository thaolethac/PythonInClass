# Bài 1
def Sum(n):
    list = n.split("_")
    sum = list[1] + list[2]
    return sum

# Bài 2
def Tiso(n):
    list = n.split("_")
    if list[1] > list[2]:
        return list[0]
    elif list[1] < list[2]:
        return list[3]
    else:
        return "Equal"
