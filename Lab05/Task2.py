# Write a function that receives a word and returns the number of ‘a’s in the word.
def a_count(string):
    asi = string.count('a')
    return asi


# Write a function that receives a word and returns the number of vowels in the word.
def vowel(string):
    no_vowel = 0
    for i in range(len(string)):
        if string[i] in "aeiou":
            no_vowel += 1
    return no_vowel


# Write a function that receives two words and returns True if they are the same length and also if they begin and end
# with the same letter, False otherwise. i.e. 'cat' and 'cot' are both 3 letters long and each begins with 'c' and ends
# with 't' i.e. 'back' and 'beak' are both 4 letters long and each begins with 'b' and ends with 'k'
def similar(s1, s2):
    if len(s1) == len(s2) and s1[0] == s2[0] and s1[-1] == s2[-1]:
        return True
    else:
        return False


# Add the function calls to this main() to test the functions.
def main():
    string_1 = input("Enter a word: ").lower()
    string_2 = input("Enter a word: ")
    number_as = a_count(string_1)
    no_vo = vowel(string_1)
    two_strings = similar(string_1, string_2)
    print(f"Number of a's {number_as}, and {no_vo} vowel's in it.")
    print(two_strings)


if __name__ == '__main__':
    main()
