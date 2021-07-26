import functions
import random

# Ask the user for a positive integer number.
# Create a list of that many random numbers between 1 and 10.
# Print a neat table consisting of each number 1 to 10 and the number of times that each number appears in the numbers.
a = []
x = functions.read_valid_integer("How many random numbers do you want to see? ")
for i in range(0, x):
    y = random.randint(1, 10)
    a.append(y)
print(a)

one = a.count(1)
two = a.count(2)
tree = a.count(3)
four = a.count(4)
five = a.count(5)
six = a.count(6)
seven = a.count(7)
eight = a.count(8)
nine = a.count(9)
ten = a.count(10)
print(f'Numbers of numbers? {x}')
print('Number      Occurrences')
print('=======================')
print(f'1\t\t\t\t{one}')
print(f'2\t\t\t\t{two}')
print(f'3\t\t\t\t{tree}')
print(f'4\t\t\t\t{four}')
print(f'5\t\t\t\t{five}')
print(f'6\t\t\t\t{six}')
print(f'7\t\t\t\t{seven}')
print(f'8\t\t\t\t{eight}')
print(f'9\t\t\t\t{nine}')
print(f'10\t\t\t\t{ten}')
print()
lista = [one, two, tree, four, five, six, seven, eight, nine, ten]
most = max(lista)
i = lista.index(most)
print(f'{i +1} appears the most ({max(lista)}) in a list of {x} numbers.')
