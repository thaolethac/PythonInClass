
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def getGreeting(self):
#         return f'{self.name} {self.age}'
    
# P1 = Person("Thao",19)

# print(P1.getGreeting())

# class Rectangle:
#     def __init__(self, length,width):
#         if(length >= width):
#             self.length = length
#             self.width = width
#         else:
#             self.length = width
#             self.width = length
#         self.area = length*width
# rec = Rectangle(10,20) 
# rec.length
# rec.area
import math
class Fraction:
    def __init__(self,numerator,denominator):
        if(denominator < 0):
            self.numerator = -numerator
            self.denominator = -denominator
        elif(denominator > 0):
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ValueError()
        
        self.value = self.numerator/self.denominator

    def __repr__(self):
        gcd = math.gcd(self.numerator,self.denominator)
        fraction = f'{int(self.numerator/gcd)}/{int(self.denominator/gcd)}'
        return fraction
    # def __add__(self,other):
    #     return Fraction(self.value + other.value)
    def __add__(self, other):
        a = self.numerator
        b = self.denominator
        a1 = other.numerator
        b1 = other.denominator
        newNumerator = a*b1 + b*a1
        newDenomination = b*b1
        
        return Fraction(newNumerator,newDenomination)
    
    def __mul__(self,other):
        a = self.numerator
        b = self.denominator
        a1 = other.numerator
        b1 = other.denominator
        newNumerator = a*a1
        newDenomination = b*b1
        return Fraction(newNumerator,newDenomination)
    def __gt__(self,other):
        a = self.numerator
        b = self.denominator
        a1 = other.numerator
        b1 = other.denominator
        return a/b > a1/b1

fracA = Fraction(2,9)
fracC = Fraction(1,9)


fracE = fracA +  fracC
print(fracE)
# repr(fraction)

# print(fraction.__repr__())

# class Data:
#     def __init__(self, value):
#         self.value = value
        
#     def __add__(self, other):
#         return Data(self.value + other.value)
# a = Data(40)
# b = Data(2)
# c = a + b
# print(c.value)
# 42