class Student:
    def __init__(self, name, age, index, exam_result):
        self.name = name
        self.age = age
        self.ID_number = index
        self.exam_result = exam_result

    def __str__(self):
        return f"{self.name} ({self.ID_number}) is {self.age} years old and got {self.exam_result}% -" \
               f" {self.passing_grade()}"

    def passing_grade(self):
        if 100 >= self.exam_result >= 40:
            return "Pass"
        else:
            return "Fail"
