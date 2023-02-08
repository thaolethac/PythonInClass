# # # # age = 2565.67612312312
# # # # print(round(age, 2))
# # # # print(f'{age:.2f}')


# # # from tokenize import Number


def FormatPassWord(n):
    isValidLength = len(n) >= 8
    countCharecter = 0
    countNumber = 0
    for i in n:
        if (ord(i) >= 97 and ord(i) <= 97+25):
            countCharecter = countCharecter + 1
        if (ord(i) >= 48 and ord(i) <= 57):
            countNumber = countNumber + 1
        else:
            countNumber = countNumber
    if (countNumber >= 2):
        hasAtLeastTwoDigits = True
    if (countCharecter >= 1):
        hasAtLeastOneAlphabetCharacter = True

    return all([isValidLength, hasAtLeastOneAlphabetCharacter, hasAtLeastTwoDigits])
def CheckPassword(n):
    while True :
        if FormatPassWord(n) == False:
            print('Truepassword')
            break;
        print('Error')
    return n                    
            
        
CheckPassword("kkakaka")
# time.sleep()