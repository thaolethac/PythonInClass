# PART1
# def f(y):
#     print(f'value = {y}')
#     return y**2
# A = [1,2,3]

# C = [value for x in A if (value := f(x)) > 2 ]
# print(C)
# PART2

# A = [1,2,-2,4]

# D = (x**3 for x in A)

# print(D, type(D))

# for x in  D:
#     print(x)
# print('hello')

# for x in  D:
#     print(x)
#PART3
# A = [1,2,3]
# B = ['a', 'b', 'c', 'd']
# C = [12,12,31]
# # C = {A[x]:B[x] for x in range(len(A))}
# # print(C)
# # C ={}
# # for x, y in zip(A,B):
# #     C[x] = y
    
# D = dict(zip(A,B,C))
# print(D)

def addSkill(singleSkill, skills= []):
    skills.append(singleSkill)
    print(skills)
    return None

addSkill("Thao")
print('Hello')
addSkill('Swim')
addSkill('Swim')