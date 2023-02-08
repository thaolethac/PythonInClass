import math
def pt2an(a1,b1,c1,a2,b2,c2):
    d = a1*b2 - a2*b1
    d1 = c1*b2 - c2*b1
    d2 = a1*c2 - a2*c1
    x = d1/d
    y = d2/d
    return [x,y]
class Point:
    def __init__(self,p1,p2):
        self.point1 = p1
        self.point2 = p2
    def __eq__(self, other):
        return (self.point1 == other.point1) and (self.point2 == other.point2) 
    

class Triangle:
    def __init__(self,p1,p2,p3):
        self.x1 = p1.point1
        self.y1 = p1.point2
        self.x2 = p2.point1
        self.y2 = p2.point2        
        self.x3 = p3.point1
        self.y3 = p3.point2
        self.AB = math.sqrt(pow(self.x1 - self.x2,2) + pow(self.y1-self.y2,2))
        self.BC = math.sqrt(pow(self.x3 - self.x2,2) + pow(self.y3-self.y2,2))   
        self.AC = math.sqrt(pow(self.x1 - self.x3,2) + pow(self.y1-self.y3,2))
        if((self.x2 - self.x3) !=0 and (self.y2 - self.y3) !=0):
            if(((self.x1 - self.x2) / (self.x2 - self.x3)) == ((self.y1 - self.y2) / (self.y2 - self.y3))):
                raise ValueError()
    def __eq__(self,other1):
        AB1 = math.sqrt(pow(other1.x1 - other1.x2,2) + pow(other1.y1-other1.y2,2))
        BC1 = math.sqrt(pow(other1.x3 - other1.x2,2) + pow(other1.y3-other1.y2,2))
        AC1 = math.sqrt(pow(other1.x1 - other1.x3,2) + pow(other1.y1-other1.y3,2))
        list1 = [AB1, BC1, AC1]
        list2 = [self.AB,self.BC,self.AC]      
          
        return sorted(list1) == sorted(list2)
    @property
    def perimeter(self):
        return self.AB + self.BC + self.AC
    @property
    def area(self):
        x = (self.AB + self.BC + self.AC)/2
        k = math.sqrt(x*(x-self.AB)*(x-self.BC)*(x-self.AC))
        return k
    def getCentroid(self):
        g1 = (self.x1 + self.x2 + self.x3) /3
        g2 = (self.y1 + self.y2 + self.y3) / 3
        return Point(g1,g2)
    def getOrthocenter(self):
        A = self.x3 - self.x2
        B = self.y3 - self.y2
        C = self.x3 - self.x1
        D = self.y3 - self.y1
        list = pt2an(A,B,A*self.x1+B*self.y1,C,D,C*self.x2+D*self.y2)
        return Point(list[0], list[1])

