# The following is the no. of millimetres of rainfall for cork for the first six months of the year. Create a list
# storing the no of millimetres of rain for each month. You can get latest info from the Met Eireann website.

amountOfRain = [117.1, 52.4, 88.8, 16.0, 137.3, 54.3]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create a bar chart to show the amount of rain. One * represents 10 millimetres of rain.
# Write out the name of the wettest and driest month.
print(f'months:\t\trainfall')
wettest_name = ""
driest_name = ""
wettest = 0
driest = amountOfRain[0]
for i in range(len(amountOfRain)):
    stars = "*" * (int(amountOfRain[i])//10)
    print(f'{months[i]:<10}{stars}')
    if amountOfRain[i] > wettest:
        wettest = amountOfRain[i]
        wettest_name = months[i]
    if amountOfRain[i] < driest:
        driest = amountOfRain[i]
        driest_name = months[i]

print(f'{wettest_name} is the wettest and {driest_name} is the driest.')
