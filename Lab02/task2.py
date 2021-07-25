# calculating the area of a circle


def area(r):
    from math import pi
    a = pi * r * r
    return a


def screen(rad, res):
    print(f"A circle of radius {rad} has an area of {res:.2f}.")


radius = float(input("What is the radius of the circle? "))
result = area(radius)
screen(radius, result)
