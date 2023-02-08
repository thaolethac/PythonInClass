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
    def __ge__(self,other):
        a = self.numerator
        b = self.denominator
        a1 = other.numerator
        b1 = other.denominator
        return a/b >= a1/b1
    def __invert__(self):
        return Fraction(self.denominator, self.numerator)
    def __neg__(self):
        return Fraction(-1*self.numerator, self.denominator)
# fracA = Fraction(3, 4)
# fracB = Fraction(2, 6)
# fracC = Fraction(-2, -8)
# fracD = Fraction(0, 1)
# # fracE = fracA + fracC
# # fracF = fracA * fracC
# fracG = -fracA
# fracH = ~fracA


