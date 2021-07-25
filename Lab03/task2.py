# program reads sides of triangle, determines and displays the type of triangle.
import functions


def display(data):
    print(data)


def get_sides_of_triangle():
    a = functions.read_positive_float("Side1 length >>> ")
    b = functions.read_positive_float("Side2 length >>> ")
    c = functions.read_positive_float("Side3 length >>> ")
    return a, b, c


def main():
    side1, side2, side3 = get_sides_of_triangle()
    type_of_triangle = functions.determine_type(side1, side2, side3)
    display(type_of_triangle)


if __name__ == '__main__':
    main()
