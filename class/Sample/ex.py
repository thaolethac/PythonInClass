
# from symbol import return_stmt


# def toString(n):
#     length = len(str((n)))
#     if (length == 1):
#         return ('00'+str(n))
#     elif (length == 2):
#         return ('0' + str(n))
#     elif (length == 3):
#         return (str(n))
#     else:
#         return -1


# print(toString(20))


# def toString1(n):
#     length = len(str((n)))
#     x = '0'
#     if (length <= 3):
#         return x*(3-length) + str(n)
#     else:
#         return


# print(toString1(0))


# def toString3(n):
#     if (len(str(n)) <= 3):
#         return '0' + toString(n)


# print(toString3(200))


# def nMonth(n):

#     if (n <= 12 & n >= 1):
#         if (n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12):
#             return 31
#         if (n == 4 or n == 6 or n == 9 or n == 11):
#             return 30
#         if ((n == 2)):
#             return 28

#     # else:
#     #     return


# print(nMonth(2))

# Bai 3




# dem = 0
# for i in range(100,1000):
#     sum = 0
#     for j in str(i):
#         sum = sum +int(j)
#         if(sum == 20):
#             dem = dem +1
#         else :
#             dem = dem
# print(dem)


# sum =0
# for i in str(201):
#     sum = sum + int(i)
# print(sum)dadawdawd

def snt(n):
    dem = 0
    for i in range(2, n):
        if (n % (i) != 0):
            dem = dem + 1
        else:
            dem = dem
    if dem == n-2:
        print('la sont')
    else:
        print('Khong')
        return


snt(13)
# for i in range(2,30) :
#    break
