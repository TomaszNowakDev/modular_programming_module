# Write a function that takes 2 parameters a list of words and a letter a, b, c, or d.
# The function creates and returns a new list of all the words that start with the letter.
def starts(words, lett):
    return [words[i] for i in range(len(words)) if words[i].startswith(lett)]


# This time you must use split() to create a list out of the string
def split_word(words, lett):
    list_words = words.split()
    return [list_words[i] for i in range(len(list_words)) if list_words[i].startswith(lett)]


# # Add the function calls to this main() to test the functions.
def main():
    dictionary = ["cat", "candy", "apple", "ant", "bed", "book"]
    string = "cat candy apple ant bed book"
    letter = input("Enter a letter a, b or c: ")
    words_letter = starts(dictionary, letter)
    splitted = split_word(string, letter)
    print(words_letter)
    print(splitted)


if __name__ == '__main__':
    main()
