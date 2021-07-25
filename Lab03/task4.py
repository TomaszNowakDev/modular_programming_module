# Program finds the area of a triangle using the Heron's formula.
import functions
import math


def get_sides_of_triangle():
    a = functions.read_positive_integer("Enter length of side a: ")
    b = functions.read_positive_integer("Enter length of side b: ")
    c = functions.read_positive_integer("Enter length of side c: ")
    return a, b, c


def determine_semi_perimeter(side_a, side_b, side_c):
    s = side_a + side_b + side_c / 2
    return s


def determine_area(perimeter, sidea, sideb, sidec):
    area = math.sqrt(perimeter * (perimeter - sidea) * (perimeter - sideb) * (perimeter - sidec))
    return area


def display(area):
    print(f"Area = {area}")


def main():
    side1, side2, side3 = get_sides_of_triangle()
    perimeter = determine_semi_perimeter(side1, side2, side3)
    area = determine_area(perimeter, side1, side2, side3)
    display(area)


if __name__ == '__main__':
    main()
