from Circle import Circle

def main():
    circle1 = Circle()
    print("The area of th circle of radius", circle1.radius, "is", circle1.getArea())
    circle2 = Circle(25)
    print("The area of th circle of radius", circle2.radius, "is", circle2.getArea())
main()