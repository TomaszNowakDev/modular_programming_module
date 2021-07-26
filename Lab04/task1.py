# lists

# Create a list called numbers containing 4 numbers.
x = [3, 5, 7, 11]
# Print out the first number in the list.
print(x[0])
# Print out the last number in the list.
print(x[-1])

# Determine length of the list
print(len(x))

# Use a loop to print each item in numbers along with their index.
for i, number in enumerate(range(len(x))):
    print(i, x[i])

# Make a copy of numbers i.e. a proper copy not just a pointer to the same address.
q = x.copy()
print(q)

# Use a loop to add 1 to all the items in numbers
for i in range(len(x)):
    x[i] = x[i] + 1
print(x)

# Use a loop to print the contents of the lists alongside each other to demonstrate that they differ by 1
print("numbers       copy")
print("==================")
for i in range(len(x)):
    print(f'{x[i]:<15}{q[i]}')
