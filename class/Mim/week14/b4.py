class WaterCan:
    def __init__(self,currentVolume, maxVolume):
        self.currentVolume = currentVolume
        self.maxVolume = maxVolume
    def pour(self,other):
        currentVolume1 = other.currentVolume
        maxVolume1 = other.maxVolume
        
        AftercurrentVolume = currentVolume1 + self.currentVolume
        
        if(self.currentVolume == 0):
            raise ValueError
        
        if(AftercurrentVolume > maxVolume1):
            other.currentVolume = maxVolume1
            self.currentVolume = self.currentVolume - maxVolume1
        else:
            other.currentVolume = AftercurrentVolume
            self.currentVolume = 0  
        
canA = WaterCan(3, 5)                                                           
canB = WaterCan(0, 2)                                                           
canC = WaterCan(1, 3)
# print(canA.pour(canB))
canA.pour(canB)
# print(canB.currentVolume)
canA.pour(canC)

print(canA.currentVolume)
print(canC.currentVolume)