class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.height * self.width
    def getPerimeter(self):
        return 2 * (self.height + self.width)

a = Rectangle(4, 40)
b = Rectangle(3.5, 35.7)
print(a.getArea())
print(a.getPerimeter())
print(b.getArea(),b.getPerimeter())
