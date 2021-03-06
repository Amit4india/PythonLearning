'''
Created on Aug 18, 2017

@author: amiti
'''
def identity(name, age):
    "This function will print name and age if called"
    print("The name of the object is ", name)
    print ("The age of the object is ", age)
    return 
# calling the above identity function and passing parameter using keywords
identity(age=32, name="Amit") # Note order of argument passing does not matter here as we are providing keys

def defaultArgument(name, age=50):
    "function definition is below"
    print("The name of the object is ", name)
    print ("The age of the object is ", age)
    return
# Calling function with both argument. This time is will print given argument
defaultArgument(name="Nimbus", age=32)
defaultArgument(name="Neha")

# passing and variable length argument
def variableArg(name, *vartuple):
    print("The name of the object is ", name)
    for var in vartuple:
        print("the value of each var is ", var)
    return
variableArg("Amit")
variableArg("Amit", 10, 20, 30)

# Example of lambda based function
sum1=lambda arg1, arg2: arg1+arg2
# calling the lambda function
print ("the value of sum from lambda function is ", sum1(10,20))
print ("The value of sum from lambda function is ",sum1(30,40))
