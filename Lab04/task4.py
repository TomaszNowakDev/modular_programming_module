# Create a list of scores and a list of judges. These are the scores awarded by judges to one set of dancers
# in a dancing competition.
scores = [9, 8, 6, 7, 6]
judges = ["Kim", "Tim", "Finn", "Lynn", "Wynn"]

# Write a loop to find out the total of all the scores and calculate the average
total = sum(scores)
suma = 0
for i in range(len(scores)):
    suma = suma + scores[i]
print(suma)
numbers_judges = len(judges)
average = total/numbers_judges
print(f'Total points: {total}, average: {average}.')

# Use the min and max functions to print the min and max values
print(f'Max {max(scores)} and min {min(scores)}')

# Using a loop print out the name of the judge(s) who awarded the lowest score
lowest = min(scores)
index_lowest = scores.index(lowest)
# if there is only one use: print(f'{lowest} {judges[index_lowest]}')

for index in range(len(scores)):
    if scores[index] == lowest:
        print(f'{lowest} {judges[index]}')

# Using a loop count the number of judges who gave a score higher than 7 and print this out.
counter = 0
for i in range(len(scores)):
    if 7 < scores[i]:
        counter += 1

print(f'Scores over 7: {counter}.')

# To progress to the next round all the scores are added together and the minimum is subtracted. The number calculated
# must be greater than 32. Your program should say whether this person will get through to the next round
next_r = total - lowest
if next_r >= 32:
    print(f'{next_r} points. Qualified for the next round!')
else:
    print(f'{next_r} points. Not qualified for the next round.')

# Write code to ask for a judge's name. Verify that judge is in the list,
# then delete all the judge's data from both lists.
judge_name = input('Judge name please >>> ')
if judge_name in judges:
    position_judge = judges.index(judge_name)
    judges.pop(position_judge)
    scores.pop(position_judge)
print(judges)
print(scores)
