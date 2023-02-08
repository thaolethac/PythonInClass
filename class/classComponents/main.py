# # class Person:
# #     def __init__(self,name, age):
# #         self.name = name
# #         self.age = age
# #         return None

# # foo = Person('Thao', 19)

# # print(foo.name)


# class Square:
#     def __init__(self,inputSide):
#         self.side = inputSide
#         self.area = inputSide**2
#         return None
#     def sayHello(self):
#         print(f'Hello Thao {self.side}')
#         return None
#     def getArea(self):
#         return self.side**2
# object = Square(12)
# print(object.side)
# print(object.sayHello())

# object.side  = 4
# print(object.getArea())
# import math
# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#         self.area = math.pi * radius*2


#         return None

# obj = Circle(12)


class CircleK:
    def __init__(self, radius):
        self._radius = radius
        self._number_ = 100
        
        return None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._radius} , {1})"

    def printNumber(self):
        print(self.__number)
        return None


obj = CircleK(10)
print(obj._radius)

obj._radius = 123
print(obj._radius)
print(obj._number_)

obj._number_ = 1000
print(obj._number_)

print(obj)

# Viết một hàm tạo ra điểm đối xứng giữa hai tọa độ
# input 10,3
# ouput -10 , 2
