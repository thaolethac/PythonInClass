# class convertTemperature:
#     def __init__(self,x,y):
#         self.value = x
#         self.thangdo = y
#         if(y != 'CtoF' and y != 'FtoC'):
#             raise ValueError
#         return None
    
# x = convertTemperature(5, 'CtoF')
# print(x)
def convertTemperature(x,y):
    if(y != 'CtoF' and y!= 'FtoC'):
        raise ValueError
    if(y == 'CtoF'):
        m = x*1.8 + 32
        return int(m)
    if(y == 'FtoC'):
        m = (x-32)/1.8
        return int(m)

print(convertTemperature(5,'CtoFd'))