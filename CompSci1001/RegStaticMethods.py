import datetime
my_date = datetime.date(2024, 10, 19)

class Employee:

    emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}{}@email.com'.format(first, last)
        Employee.emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    

class Manager(Employee):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)

        if emps is None:
            self.emps = []
        else:
            self.emps = emps
    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emp(self):
        for emp in self.emps:
            print("-->", emp.fullename())

dev_1 = Developer('Tim', "Li", 10000, 'Python')

man_1 = Manager("Dan", "He", 90000, [dev_1])
print(man_1.email)