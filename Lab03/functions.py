# Tomasz Nowak
# Useful Functions
import math
import random
import string


def read_valid_percentage(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if 0 <= user_input <= 100:
                return user_input
            else:
                print("Values between 0-100 please.")
        except ValueError:
            print("Numbers only please.")


def read_positive_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if 0 <= user_input:
                return user_input
            else:
                print("Enter positive float number.")
        except ValueError:
            print("Numbers only please.")


def read_valid_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Whole numbers only please.")


def read_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            print("Whole positive numbers only please.")


def list_numbers_1and10(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return [random.randint(1, 10) for i in range(user_input)]
        except ValueError:
            print("Whole positive numbers only please.")


def read_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0 and user_input.isalpha():
            return user_input


def remove_punctuation(s):
    w = ''
    for i in range(len(s)):
        if s[i] in string.punctuation:
            w = w + ''
        else:
            w = w + s[i]
    return w


def valid_day_of_week(prompt):
    while True:
        days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
        user_input = input(prompt).lower()
        if user_input in days:
            return user_input


def determine_type(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return "The lengths you have entered can not make a triangle!"
    else:
        print("The lengths you entered can make triangle!")
        if a == b == c:
            return "It is equilateral triangle (all sides equal)."
        elif a == b or a == c or b == c:
            return "It is isosceles triangle (two sides equal)."
        else:
            return "It is scalene triangle (no sides equal)."


def determine_hypotenuse(s1, s2):
    x = math.sqrt((s1**2) + (s2**2))
    return x


def determine_semi_perimeter(side_a, side_b, side_c):
    s = side_a + side_b + side_c / 2
    return s


def determine_area(perimeter, sidea, sideb, sidec):
    area = math.sqrt(perimeter * (perimeter - sidea) * (perimeter - sideb) * (perimeter - sidec))
    return area
