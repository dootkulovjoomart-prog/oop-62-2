class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def get_salary(self):
        return f' My salary is {self.salary}'
    def get_role(self):
        return f' My names {self.name} and  i am employee'
    def get_info(self):
        return f'Name: {self.name} ,role: Employee  Salary: {self.salary}'

class BackendDeveloper(Employee):
    def __init__(self,level, name, salary):
        super(BackendDeveloper, self).__init__(name , salary)
        self.level = level

    def get_info(self):
        return f'Name: {self.name} ,role: BackendDeveloper  Salary: {self.salary}'

    def get_salary(self):
        return f' My names {self.name} and  i am BackendDeveloper'


    def get_salary(self):
        if self.level == 'junior':
            return self.salary
        elif self.level == 'middle':
            return int(self.salary * 1.2 )
        elif self.level == 'senior':
            return int(self.salary * 1.5 )
class Manager(Employee):
    def __init__(self, team_size,  name, salary):
        super(Manager, self).__init__(name , salary)
        self.team_size = team_size

    def get_role(self):
        return 'manager'

    def get_salary(self):
        return self.salary + self.team_size * 100

    def get_info(self):
        return f'Name: {self.name} ,role: Manager  Salary: {self.salary}'

class Intern(Employee):
    def __init__(self,months, name, salary):
        super(Intern, self).__init__(name,salary)
        self.months = months


    def get_role(self):
        return 'intern'

    def get_salary(self):
        return self.salary

    def get_info(self):
        return f'Name: {self.name} ,role: Intern  Salary: {self.salary}'




employees = [
    Intern(1, 'John', 121121),
    Manager(30, 'Akyl', 2000),
    BackendDeveloper('senior' , 'artem' , 4000),
    Employee('John' , 50000),
]


for emp in employees:
    print(emp.get_info())


