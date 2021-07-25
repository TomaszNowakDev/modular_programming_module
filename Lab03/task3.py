# program reads two sides of a right-angled triangle and determines and displays the length of the hypotenuse using
# use the Pythagorean theorem.
import functions
from math import sqrt


def get_sides_of_triangle():
    a = functions.read_positive_integer("Enter length of side a: ")
    b = functions.read_positive_integer("Enter length of side b: ")
    return a, b


def determine_hypotenuse(s1, s2):
    x = sqrt((s1**2) + (s2**2))
    return x


def display(hypo):
    print(f'Hypotenuse of that triangle is {hypo:.2f}.')


def main():
    side_1, side_2 = get_sides_of_triangle()
    hypotenuse = determine_hypotenuse(side_1, side_2)
    display(hypotenuse)


if __name__ == '__main__':
    main()
