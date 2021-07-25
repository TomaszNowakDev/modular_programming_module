# the program assigns the grades to the points scored by the students saved in the file.txt
def file(name):
    with open(f"{name}.txt", 'r') as opened_file:
        for line in opened_file:
            one_line = line.rstrip()
            mark = int(one_line)
            print(f"{mark}% - {grade(mark)}")


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


file_name = input("What is the name of a file? ")
file(file_name)
