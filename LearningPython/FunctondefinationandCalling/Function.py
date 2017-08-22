'''
Created on Aug 18, 2017

@author: amiti
'''
def amit(str1):
    "defining the function here"
    str1.append([10,20,30])
    print("the value of str inside the amit function", str1)
    return str1;
str1=[1,2,3,4]
print("The value of str1 before calling the amit function ", str1)
amit(str1); # calling the function
print("the value of str1 outside the amit function is", str1)
