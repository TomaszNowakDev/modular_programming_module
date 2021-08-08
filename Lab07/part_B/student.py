from student_class import Student


def display(items):
    for item in range(len(items)):
        print(f"{item+1}. {items[item]}")


def average(stud):
    x = [st.exam_result for st in stud]
    average_num = sum(x) / len(stud)
    return average_num


def students_details(details):
    with open("students.txt", 'w') as file:
        for student in details:
            print(student, file=file)


def main():
    s1 = Student("Fred Bloggs", 21, "R0001234567", 75)
    s2 = Student("Mickey Mouse", 19, "R0007654321", 38)
    s3 = Student("Minnie Mouse", 18, "R000123546", 56)
    students = [s1, s2, s3]
    display(students)
    average_result = average(students)
    print(f"Average in the class is {average_result:.2f}%")

    students_details(students)


if __name__ == '__main__':
    main()
