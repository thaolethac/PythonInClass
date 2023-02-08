import math


class Point:
    def __init__(self, abscissa, ordinate):
        self.x = abscissa
        self.y = ordinate

    def distancePointToPoint(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        dis = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        return dis


pointA = Point(3,5)

pointB = Point(-1,2)
pointC = Point(-4,6)

pointD = Point(-1,2)

# dist = pointA.distancePointToPoint(pointB)

# print(dist)
class Line:
    def __init__(self, m, n):
        self.point1 = m
        self.point2 = n
        if (self.point1.x == self.point2.x) and (self.point1.y == self.point2.y):
            raise ValueError

    # def LineofTwoPoints(self):

    def distanceLineToPoint(self, other):
        x3 = other.x
        y3 = other.y
        if (self.point1.x - self.point2.x) == 0:
            dist = abs(self.point1.x - x3)
            return dist
        elif (self.point1.y - self.point2.y) == 0:
            dist = abs(self.point1.y - y3)
            return dist
        else:
            a = (self.point1.y - self.point2.y) / (self.point1.x - self.point2.x)
            b = (self.point2.y * self.point1.x - self.point1.y * self.point2.x) / (
                (self.point1.x - self.point2.x)
            )
            dist = abs(
                (a * x3 + b - y3)
                / (math.sqrt(pow(a, 2) + 1))
            )
            # e = (math.sqrt(pow(a, 2) + pow(b, 2)))
            # if(int(dist - int(dist)) == 0 ):
            #     return int(dist)
            # else:
            return dist
            # return e


lineAB = Line(pointA, pointB)

dist = lineAB.distanceLineToPoint(pointC)
# lineBD = Line(pointB,pointD)
print(dist)

