from student_class import Student


def display(items):
    for item in range(len(items)):
        print(f"{items[item]}")


def students_details(d):
    with open("students.txt", 'w') as file:
        for student in d:
            print(student, file=file)


def fail(studs):
    f = []
    for i in range(len(studs)):
        if studs[i].exam_result < 40:
            f.append(studs[i].name)
    return f


# def fail_2(studs):
#    return [student.name for student in studs if student.exam_result < 40]


def main():
    with open("students_from_file.csv") as inputs:
        lines = inputs.readlines()
        students = []
        for line in lines:
            split_line = line.split(",")
            name = split_line[0]
            student_id = split_line[1]
            age = int(split_line[2])
            exam_result = int(split_line[3])
            student = Student(name, age, student_id, exam_result)
            students.append(student)
    display(students)
    x = fail(students)
    display(x)


if __name__ == '__main__':
    main()
