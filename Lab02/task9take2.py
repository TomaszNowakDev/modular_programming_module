# Program reads scores from the file.txt assigns grades and saves output in file2.txt
def ask(name_entered):
    file_name = input(name_entered)
    return file_name


def grade(score):
    if score < 40:
        return "Fail"
    elif 40 <= score < 50:
        return "Pass"
    elif 50 <= score < 60:
        return "H22"
    elif 60 <= score < 70:
        return "H21"
    else:
        return "H1"


def main():
    f_name = ask("What is the name of file with exam results? ")
    with open(f"{f_name}.txt", 'r') as opened_file:
        writing = ""
        for line in opened_file:
            one_line = line.rstrip()
            mark = int(one_line)
            print(f"{mark}% - {grade(mark)}")
            writing += f"{mark}% - {grade(mark)}\n"
    f_name = ask("What is the name of file you want store results in? ")
    with open(f"{f_name}.txt", 'w') as write_to_file:
        print(writing, file=write_to_file)


main()
