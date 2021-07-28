# Write a function that receives two lists, A and B (which are the same length) and returns the difference
# between them.

def subtraction(x1, x2):
    # resu = []
    # for i in range(len(x1)):
    # y = resu.append(x1[i] - x2[i])
    # return resu
    return [x1[i] - x2[i] for i in range(len(x2))]


def main():
    numbers_1 = [1, 12, 71, 33, 76, 70, 12]
    numbers_2 = [10, 2, 37, 34, 61, 7, 12]
    result = subtraction(numbers_1, numbers_2)
    print(result)


if __name__ == '__main__':
    main()
