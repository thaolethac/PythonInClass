# Example

import random
thislist = ["apple", "banana", "cherry"]
print(thislist[int(random.random()*3)])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Inf(a):
        print('Tôi tên là :' + a.name)
        print('Năm nay tôi ' + str(a.age) + ' tuổi')


p1 = Person('Thao', 19)
# print(p1.name)
# print(p1.age)

p1.Inf()

# Bài 1
import datetime as date
now = date.datetime.now()
nowyear = now.year
birthday = 2003

print("Tuổi của bạn là : " + str(nowyear - birthday))

# Work
count = 0
name = 'Anivia haha'
for x in name.upper():
    if (x != ' '):
        count = count +1
    if(x == ' '):
     count  = count
    

print(count)
print(name.upper().count('A'))
print(name.lower().count('a'))
# name.split(' ')
# Array

myArray = ['Le', 'Thac', 'Thao']
myArray[0] = 'Heehe'
Json = [{   
    'fname' : 'Thao',
    'lname' : 'Le'
},
        {
        'fname' : 'haha',
        'lname' : 'bla'
        }
]

print(Json[1])
char = ""