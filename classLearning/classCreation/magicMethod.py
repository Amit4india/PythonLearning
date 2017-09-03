'''
Created on Sep 3, 2017

@author: amiti
'''
# Suppose in our employee class we simply wants to put add functionality which 
# will return add of two employee salary
# Also we want to return user the total number of character present in FullName


class Employee:
    def __init__(self, first, last , pay):
        self.first = first
        self.last= last
        self.pay=pay
    # Defining a special dunder method to add pay of two employee
    def __add__(self, other):
        return self.pay + other.pay 
    
    # Defining special dunder method to return no of character in FullName of emp
    def __len__(self):
        return len(self.FullName())
    
    # Defining a normal method to return full name of the employee
    def FullName(self):
        return '{} {}'.format(self.first, self.last)
    
    # Defining a special method to print entire parameter pass during instance
    # creation
    def __repr__(self):
        return '{} {} {}'.format(self.first, self.last, self.pay)    

emp1 = Employee('Amit', 'srivastava', 5000)
emp2 = Employee('Niahrika','Narula', 6000)
print(emp1)
print(emp2)
print(emp1.FullName())
print(emp2.FullName())
print(emp1+emp2)
print(emp1.__len__())

