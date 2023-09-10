

import math
import sys

class shape:
    def area(self):
        pass
class Triangle(shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height
class Rectangle(shape):
    def __init__(self, length,width):
        self.width=width
        self.length=length
    def area(self):
        return self.length * self.width
class Circle(shape):
    def __init__(self, Radius):
        self.Radius=Radius

    def area(self):
        return math.pi * self.Radius ** 2


while True:
    print("1.tri\t2.rect\t3.cir\n")
    choice = int(input())
    if choice==1:
        b=int(input("base"))
        h=int(input("height"))
        triangle=Triangle(b,h)
        print("Area is",triangle.area())
    elif choice==2:
        l=int(input("lenght"))
        w=int(input("width"))
        rectangle=Rectangle(l,w)
        print("Area is",rectangle.area())
    elif  choice==3:
        r=float(input("radius"))
        circle=Circle(r)
        print("Area is",circle.area())
    else:
        print(" invalid enter aa valid choice")
        sys.exit(0)