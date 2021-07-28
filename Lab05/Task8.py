# Write a function that returns the product of a number, c, and an n-dimensional vector, A, represented as a list
# create a new list which will become each number in the original list just multiplied by c.
def jakas(x):
    return [x[i] * 6 for i in range(len(x))]


def main():
    list_numbers = [1, 2, 4, 6, 8, 97]
    print(jakas(list_numbers))


if __name__ == '__main__':
    main()
