class Dice:
    def __init__(self, tup):
        self.dice = tup

    def compare(self, other):
        x = other.dice
        countA = 0
        countB = 0
        for i in self.dice:
            for j in x:
                if i > j:
                    countA += 1
                elif i < j:
                    countB += 1
        if countA > countB:
            return 1
        elif countA < countB:
            return -1
        else:
            return 0


diceA = Dice((1, 2, 3, 4, 5, 6))
diceB = Dice((2, 3, 2, 4, 2, 5))

value = diceA.compare(diceB)

print(value)
