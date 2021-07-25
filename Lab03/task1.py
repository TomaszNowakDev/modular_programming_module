# Program gets 3 scores and calculates average, assign grade.
import functions


def main():
    exam1, exam2, exam3 = read_exams()
    average = calculate_average(exam1, exam2, exam3)
    grade = determine_grade(average)
    display(average, grade)


def read_exams():
    a = functions.read_valid_percentage("What is the mark for the first exam? ")
    b = functions.read_valid_percentage("What is the mark for the second exam? ")
    c = functions.read_valid_percentage("What is the mark for the third exam? ")
    return a, b, c


def calculate_average(a, b, c):
    avr = (a + b + c)/3
    return avr


def determine_grade(average):
    if 0 <= average <= 39:
        g = 'Failing'
    elif 40 <= average <= 69:
        g = 'Acceptable'
    else:
        g = 'Excellent'
    return g


def display(avr, gra):
    print(f'{avr:.2f}% - {gra}')


main()
