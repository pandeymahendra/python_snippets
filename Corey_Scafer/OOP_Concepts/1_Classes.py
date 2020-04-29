# Python OOP Concepts


class Employee():
    raise_amount = 1.02     # Class Variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'example.com'
        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # Class variables must be accessed through either class or through an instance
        # self.pay = int(self.pay * self.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

################################################################


print("Employee Raise Amount Defines in Class", Employee.raise_amount)

emp1 = Employee('Mahendra', 'Pandey', 10000)
emp2 = Employee('John', 'Smith', 20000)

Employee.raise_amount = 1.04

print('----------------------------------------')

print(emp1.first)
print(emp1.last)
print(emp1.email)
print("Basic Pay: ", emp1.pay)
emp1.apply_raise()
print("Raised Pay: ", emp1.pay)
print(emp1.full_name())

print('----------------------------------------')
emp1.raise_amount = 1.10
print(emp2.first)
print(emp2.last)
print(emp2.email)
print("Basic Pay: ", emp2.pay)
emp2.apply_raise()
print("Raised Pay: ", emp2.pay)
print(emp2.full_name())
# print(emp2.__dict__)
print('----------------------------------------')
print("Class Raise Amount:", Employee.raise_amount)
# print(Employee.__dict__)
print("emp1 Raise Amount:", emp1.raise_amount)
print("emp2 Raise Amount:", emp2.raise_amount)

print("Number of Employees:", Employee.num_of_emps)
# Employee.num_of_emps, is a class variable defined in __init__ as it will not be used by an individual instance
#
