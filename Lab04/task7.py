import functions
import random

# Ask the user for a positive integer number.
a = []
x = functions.read_valid_integer("How many random numbers do you want to see? ")

# Create a list of that many random numbers between 1 and 10.
for i in range(0, x):
    y = random.randint(1, 10)
    a.append(y)
print(a)

# Write code to create a new list consisting only of the even numbers in the list.
even_no = []
for i in range(len(a)):
    if (a[i] % 2) == 0:
        even_no.append(a[i])
# Write code to display the number of even numbers in the list.
print(len(even_no))

# Write code to display the number of odd numbers in the list. printing them in one line
no_odd = 0
for i in range(len(a)):
    if (a[i] % 2) != 0:
        no_odd += 1
        print(a[i], end=', ')

print("\nNo of odd numbers in the list:", no_odd)

# Write code to determine how many times 10 appears in the list.
tens = a.count(10)
print()
print(f'Tens in the list {tens}.')

# Write code to delete all the numbers that are multiples of 3 from the list.
for i in a:
    if i % 3 == 0:
        a.remove(i)
print(a)
