# Ask the user to enter the names of 4 runners and add them to a list called runners
# For each runner ask the user to enter the time taken by each runner in seconds.
runners = []
times = []
for i in range(4):
    runner = input("Enter a nme of a runner: ")
    runners.append(runner)
for i in range(len(runners)):
    time = int(input("What is the run time: "))
    times.append(time)

# Find the winning time and print out the winner's name.
# Deal with the situation where there is a draw for first place.
#  Print out the how many seconds behind the winner each of the other runners came.
fastest = min(times)
index_lowest = times.index(fastest)
for index in range(len(runners)):
    if times[index] == fastest:
        print(f'{fastest}s. {runners[index]}')
for i in range(len(times)):
    behind = times[i] - fastest
    if behind == 0:
        print(f'{runners[i]} is the winner, with time {fastest}s.')
    else:
        print(f'{runners[i]}, {behind}s behind winner.')
