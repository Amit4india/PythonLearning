'''
Created on Sep 1, 2017

@author: amiti
'''
class employee: # This is how we declare class
    def __init__(self, firstName, lastName, pay): # This is kind of constructor in Python
        # By default every method in python class will take self (instance)as first arg
        self.firstName=firstName  # equivalent to this key word
        self.lastName=lastName
        self.pay=pay
        self.email= firstName + '.' + lastName + "@gmail.com"
    
    def fullName(self):
        print('{} {}'.format(self.firstName, self.lastName))
    # Here function is returing none
empA1= employee('Amit','Srivastava',700000)
print(empA1.email)
empA1.fullName()
        