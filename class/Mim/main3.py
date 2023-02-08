
# __repr__() is called when the object is passed to print() method
fracA = Fraction(3, 4)
assert fracA.__repr__() == '3/4'
assert fracA.value == 0.75

fracB = Fraction(2, 6)
assert fracB.__repr__() == '1/3'

fracC = Fraction(-2, -8)
assert fracC.__repr__() == '1/4'

fracD = Fraction(0, 10)
assert fracD.__repr__() == '0/1'

fracE = fracA + fracC
assert fracE.__repr__() == '1/1'
assert fracE.value == 1

fracF = fracA * fracC
assert fracF.__repr__() == '3/16'
assert fracF.value == 0.1875

fracG = -fracA
assert fracG.__repr__() == '-3/4'

fracH = ~fracA
assert fracH.__repr__() == '4/3'

assert fracA > fracB
assert fracA >= fracB
assert fracC < fracB
assert fracC <= fracB

try:
    fracI = Fraction(1, 0)
except ValueError:
    # the object Fraction(1, 0) must cause a ValueError
    pass
else:
    assert False

