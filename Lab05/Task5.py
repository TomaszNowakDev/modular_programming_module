# Write a function that receives a list and returns True if the values stored in the list are in ascending order
# and False otherwise.
def ascending(x):
    for i in range(len(x) - 1):
        if x[i] >= x[i+1]:
            return False
    return True


def main():
    numbers = [1, 2, 3, 5, 6, 7, 12]
    name = ascending(numbers)
    print(name)


if __name__ == '__main__':
    main()
