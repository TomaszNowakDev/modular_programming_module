import functions
import random

# Write code to ask the user for a positive integer number (why not re-use a function?) and create a list containing
# that many random integer numbers between 0 and 100
a = []
x = functions.read_valid_integer("How many random numbers do you want to see? ")
for i in range(0, x):
    y = random.randint(1, 100)
    a.append(y)
print(a)

# Replace the last two items in the list with 0s.
a[-1] = 0
a[-2] = 0

# Use a loop to print the items in the list along with each index.
for i in range(len(a)):
    print(f'{i}.\t{a[i]}')

# Reverse all the items in the list
a.reverse()
print(a)

# sum all items in the list
s = sum(a)
print(s)

# Count and print the number of times 50 appears in the list.
app = a.count(50)
print(app)

# Count and print the number of times a number 50 or over appears in the list.
counter = 0
for i in range(len(a)):
    if 50 <= a[i] <= 100:
        counter += 1
print(counter)
