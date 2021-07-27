import random
import functions


# Write a function that receives an number and returns a list containing that many (random) numbers between 1 and 10.
def list_numbers_1and10(x):
    return [random.randint(1, 10) for i in range(x)]


def main():
    numbers = functions.read_valid_integer("How many random numbers do you want to see? ")
    a = list_numbers_1and10(numbers)
    print(a)


if __name__ == '__main__':
    main()
