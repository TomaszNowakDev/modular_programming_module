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

counters = [0] * 10
for item in a:
    for q in range(0, 10):
        if item == q + 1:
            counters[q] += 1

print(f'Here with for loop {counters}')
print(f'Numbers of numbers? {x}')
print('Number      Occurrences')
print('=======================')
for i in range(len(counters)):
    print(f"{i+1}{counters[i]:>15}")

most_common = max(counters)
most_index = counters.index(most_common)
print(f"Most common is number: {most_index + 1}")
# the second method if there are several common numbers
common = []
for i in range(len(counters)):
    if counters[i] == most_common:
        common.append(i + 1)

print(f"Most common is/ are: {common}")
