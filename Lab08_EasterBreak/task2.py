class Employee:
    def __init__(self, employee_id, first_name, last_name, hourly_rate):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"ID = {self.employee_id}, First name = {self.first_name}, Last name = {self.last_name}," \
               + f"Hourly rate = {self.hourly_rate}"


def main():
    e1 = Employee(34574, "John", "Beans", 18.04)
    e2 = Employee(456784, "Kevin", "Murphy", 12)
    e3 = Employee(input("Enter employee ID =>"), input("Employee first name: =>"), input("Employee last name: =>"),
                  input("Employee hourly rate: =>"))
    employees = [e1, e2, e3]
    for e in employees:
        print(e)


if __name__ == '__main__':
    main()
