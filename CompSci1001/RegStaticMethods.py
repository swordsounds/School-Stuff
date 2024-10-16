class Employee:

    emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        pass

    
emp_1 = Employee("Tim", "Li", 100000)
emp_2 = Employee("Dan", "Man", 910000)

emp_1.apply_raise()

print(emp_1.pay)