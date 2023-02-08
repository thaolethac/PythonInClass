import math
def haha(x):
    if x == 1:
        return 1
    return haha(x-1)/2 + 1/haha(x-1)

print(haha(13))