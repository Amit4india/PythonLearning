'''
Created on Sep 2, 2017

@author: amiti
'''
class employee:
    raiseAmt=1.05 # Class variable 
    no_of_emp=0 # class variable
    def __init__(self, fName, lName, pay): # fname, lName, pay >> instance variable
        self.fName=fName
        self.lName=lName
        self.pay=pay
        self.email=fName+'.'+ lName+'@amt.com'
        employee.no_of_emp +=1 # Class Variable which need no modifications
        
    def fullName(self):
        print('{} {}'.format(self.fName, self.lName))
    def RaiseAmt(self):
        self.pay=int(self.pay*self.raiseAmt)
        return self.pay

emp1=employee('Amit', 'Srivastava',50000)
emp2=employee('bunny', 'narula', 600000)
emp1.fullName()
print(emp1.RaiseAmt())
#emp1.raiseAmt=2
print(emp1.RaiseAmt())
print(emp1.__dict__)  # print the namespace of instance emp1
print(employee.__dict__) # print the namespace of class employee
print(emp1.no_of_emp)
        