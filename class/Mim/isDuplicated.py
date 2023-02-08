def isDuplicated(tup):
        for i in tup:
            if(tup.count(i) > 1):
                return True
            return False



# print()

tup = (1,2)

print(isDuplicated(tup))    
# list = [tup] 
    