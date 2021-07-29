# Write a function that takes in a list of names and ages and returns two new lists with the names and ages
# of the children over 5.
def check(n, a):
    over_n = []
    over_a = []
    for i in range(len(n)):
        if a[i] >= 5:
            over_n.append(n[i])
            over_a.append(a[i])
    return over_n, over_a


# Write a main() function that creates 2 lists, a list of children's names and a list of their ages (integers)
# and demonstrate how the function might be used.
def main():
    names = ['Tim', 'Marcel', 'Kevin', 'John', 'Ted']
    ages = [5, 6, 4, 11, 3]
    over5_n, over5_a = check(names, ages)
    print(over5_n, over5_a)


if __name__ == '__main__':
    main()
