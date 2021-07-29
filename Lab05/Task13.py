import functions
# Write a function that takes a string as a parameter and the number of three letter words in this string.


def length(st, num):
    s = functions.remove_punctuation(st)
    s_list = s.split()
    counter = 0
    for i in range(len(s_list)):
        if len(s_list[i]) == num:
            counter += 1
    return counter


def main():
    sting = "I know some new trick, said the cat in the hat. A lot of good tricks."
    number = 3
    catch = length(sting, number)
    print(f'There is {catch} three letter words in the sentence.')


main()
