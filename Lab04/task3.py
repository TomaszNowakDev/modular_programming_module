# Create a list called countries containing a list of 4 countries.
countries = ["spain", "brazil", "portugal", "bolivia"]

# Use a loop to change each country so that it is in proper case.
for i in range(len(countries)):
    countries[i] = countries[i].capitalize()

# append italy to the end of the list
countries.append("italy")
print(countries)

# Remove "Bolivia" from the list
countries.remove("Bolivia")
print(countries)

# Ask the user for the name of a country and append it if it is not already in the list.
# Ask them again if it is already in the list.
while True:
    x = input("What country would you like add to the list? ")
    if x not in countries:
        countries.append(x)
        break
print(countries)

# Divide the list into two lists and print them out in a loo[
group1 = countries[0:2]
group2 = countries[2:]
for i in range(0, len(group1)):
    print(group1[i])
print('---------------------------')
for i in range(0, len(group2)):
    print(group2[i])
