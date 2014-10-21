#Find the area of a circle, square, and triangle

#Triangle = (A=B*H/2)
#Square = B x H
#Circle = pi R 2
import time
import math
import sys

def calc():
    shape = input("Circle, Square, or Triangle?")
    if shape.lower() == "circle":
        rad = int(input("Enter the radius of the circle"))
        pi = float(math.pi)
        area = float((rad*rad)*pi)
        #rounded = round(area, 3)
        print("The area of your circle is", area)
    elif shape.lower() == "square":
        L = int(input("Enter Length or Height"))
        area = float(L*L)
        print(area)
    elif shape.lower() == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the Height: "))
        area = float((base*height)/2)
        print("The area of your triangle is.. ", area)
calc()




