
    
def isPalindrome(n):
    length = len(str(n))
    stringN = str(n)        
    if(length  == 1):
        return True
    if(length % 2 ==0):
        for i in range(0,length):
            if((int(stringN[i]) != int(stringN[length-1-i]))):
                return False
            return True
    else:
        for i in range(0,length):
            if(i != int(length/2)):
                if(int(stringN[i]) != int(stringN[length-1-i])):
                    return False
                return True


print(isPalindrome(1123213))
