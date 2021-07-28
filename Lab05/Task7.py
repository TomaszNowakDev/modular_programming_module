# Write a function that returns the magnitude of an n-dimensional vector represented as a list go through each number
# in the list, squaring and adding as you go. Find the square root of the result and return it.
import math


def vector_represented(x):
    a = 0
    for i in range(len(x)):
        a = a + x[i]**2
    return math.sqrt(a)


def main():
    list_numbers = [1, 2, 4, 6, 8, 97]
    print(f'{vector_represented(list_numbers):.2f}')


if __name__ == '__main__':
    main()
