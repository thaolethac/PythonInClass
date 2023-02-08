

# # foo = {1, 2, 32, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2}

# # bar = {3, 2, 1, 100}

# # print(foo < bar)


# import sqlite3


# dictA = {
#     'name': 'Thao', 'age': 19, 'height': 50,

# }

# dictB = {
#     'name': 'Thao', 'age': 19, 'height': 50,

# }
# listD = [dictA, dictB]

# print(*listD, sep='\n')

# print('hello', end='')
# print('thao', end='')


def Finonacci(n):
    def F_Memo(n, memo):
        if n in memo:
            return memo[n]
        x = F_Memo(n-1, memo) + F_Memo(n-2, memo)
        memo[n] = x
        return x
    memo = {0: 1, 1: 1, 2: 1}
    return F_Memo(n, memo)
print(Finonacci(999))


# memo  = {2: 5, 4: 6}

# print(5 in memo)
