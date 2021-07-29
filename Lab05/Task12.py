import functions
# The function returns a list of words that are the specified length found in the string.


def length(st, num):
    s = functions.remove_punctuation(st)
    s_list = s.split()
    return [s_list[i] for i in range(len(s_list)) if len(s_list[i]) == num]


def main():
    sting = "I know some new trick, said the cat in the hat. A lot of good tricks."
    number = 5
    catch = length(sting, number)
    print(catch)


if __name__ == '__main__':
    main()
