# import math


# class RightTriangle:
#     def __init__(self, legA, legB):
#         self.legA = legA
#         self.legB = legB
#     def getHypotenuse(self):
#         return (math.sqrt(self.legA**2 + self.legB**2))
#     def getPerimeter(self):
#         return self.legA + self.legB + self.getHypotenuse()

#     def getArea(self):
#         return 1 / 2 * self.legA * self.legB


# Side = RightTriangle(3,4)

# # print(Side.getPerimeter())
# # print(Side.getArea())

# print("After change Side in Triangle")
# print(Side.getPerimeter())
# print(Side.getArea())


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


obj = Point2D(1, 2)
print(obj.x)
