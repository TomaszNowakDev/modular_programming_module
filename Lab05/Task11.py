import string

# Write a function that receives a string.
# The function should return a copy of the string but with all the punctuation removed.


def remove_punctuation(s):
    w = ''
    for i in range(len(s)):
        if s[i] in string.punctuation:
            w = w + ''
        else:
            w = w + s[i]
    return w


def main():
    sti = "I know some new trick, said the cat in the hat. A lot of good tricks."
    catch = remove_punctuation(sti)
    print(catch)


if __name__ == '__main__':
    main()
