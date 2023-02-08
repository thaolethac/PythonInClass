class Rectangle:
    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)
         
        return None
    @property
    def area(self):
        return self.length * self.width
    @property
    def perimeter(self):
        return (self.length + self.width) * 2


