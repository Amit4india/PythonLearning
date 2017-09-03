'''
Created on Sep 2, 2017

@author: amiti
'''
# Objective here is to create an employee class an developer class and manager class
# Developer and manager are subclasses of Employee class
# Developer class has special raise_amt value which only applies to dev emp1
# Developer class has one more argument which tell type of lang emp has
# Manager class have one argument which tell what emp it has

class Employee:
    amt_raise = 1.05
    # below is kind of constructor which use instance to initialize class variable
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=int (pay)
    # FullName method will print full name of employee.
    def FullName(self):
        print ('{} {}'.format(self.first, self.last))
    # RaiseAmt method will apply raise on pay amount
    def RaiseAmt(self):
        self.pay=  int (self.pay * self.amt_raise)
        return self.pay
        
# creating a class method to return above class variable as object in case 
# user provide string  
    @classmethod
    def emp_String(cls, str):
        first, last, pay = str.split('-')
        return cls(first, last, pay)
       
    
# Static method use for special function which need to support from instance VARIABLE
# Static method will have no self argument 
    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            print ("Weekend enjoy holiday")
        else:
            print ("work hard dear holiday will come soon")

# Creating a developer class
class Developer(Employee):
    #  changing raise amount here
    amt_raise=1.10
    # Defining new init method for added argument functionality
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang=lang
# Creating Manager class 
class Manager(Employee):
    amt_raise=2
    # Defining new init for new added functionality
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    # adding method add emp for help
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    # adding remove method
    def remove_emp(self, emp): 
        if emp in self.employees:
            self.employees.remover(emp)
    def print_employee(self):
        for emp in self.employees:
            emp.FullName()                  
# Now creating instance of all class to perform certain operation

st1= 'Bunny-Narula-70000'
# Creating instance of emp1 from string given using classMethod emp_String()
emp1 = Employee.emp_String(st1)
emp1.FullName()
print(emp1.RaiseAmt())

# Creating instance of developer class
emp2 = Developer("Amit","Srivastava",900000,"Python")
emp2.FullName()
# Raising amount to developer
print(emp2.RaiseAmt())

# Creating manager class
emp3 = Manager("mudit","Seth", 50000, [emp2])
emp3.FullName()
print(emp3.RaiseAmt())
emp3.add_emp(emp2)
emp3.add_emp(emp1)
emp3.print_employee()
    