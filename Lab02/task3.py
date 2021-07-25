# This program calculates surface area of the cylinder
def area(r, h):
    import math
    surface = (2 * math.pi * r * h) + 2 * math.pi * r * r
    return surface


def info(local_a, local_b, local_surface_area):
    print(f"Radius is {local_a}, high is {local_b}, "
          f"and surface area of the cylinder is {local_surface_area:.2f}")


a = float(input("What is the radius of the cylinder? "))
b = float(input("What is the high of the cylinder? "))
surface_area = area(a, b)
info(a, b, surface_area)
