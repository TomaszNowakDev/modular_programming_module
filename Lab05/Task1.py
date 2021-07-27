# Tomasz Nowak

# Write a function that receives one parameter, a list of race times. The function should return one value,
# the average race time achieved by all entrants.
def one_parameter(times):
    aver = sum(times) / len(times)
    return aver


# Write a function that receives two list as parameters. The first is a list of names and the second is a list of
# race times. The function should return a list of the names of those people whose times are greater than 25 minutes.
def over25(na, times):
    more25 = []
    for i in range(len(times)):
        if times[i] > 25:
            more25.append(na[i])
    return more25
    # or return [na[i] for i in range(len(times)) if times[i] > 25]


# Write a function that receives one parameter, a list of race times. The function should modify the list of race times
# so they are all 10% faster.
def reduced(times):
    for i in range(len(times)):
        times[i] = times[i] * 0.9


# Write a function that receives two lists as parameters. The first is a list of names and the second is a list of race
# times. The function should display the list of names and times in a suitable formatted table.
def display(name, times):
    print(f"{'Name':10}{'Time'}")
    print('=====================')
    for i in range(len(name)):
        print(f'{name[i]:10}{times[i]:.2f}min')


def main():
    time_taken = [32, 27, 23, 26, 26, 18]
    average = one_parameter(time_taken)
    names = ["Ann", "Joe", "Pat", "Ken", "Ali", "Ger"]
    greater_than_25 = over25(names, time_taken)
    reduced(time_taken)
    display(names, time_taken)
    print(f'Average is {average:.2f}min. Times over 25min {greater_than_25}')


# Add the function calls to this main() to test the functions.
if __name__ == '__main__':
    main()
