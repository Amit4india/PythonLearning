'''
Created on Aug 20, 2017

@author: amiti
'''
# with method can be use to open the file. This method will take care of closing the file
def MethodsOfFileOpening():
    try:
        file1=open("C:\Eclipse\Workspace\LearningPython\SampleReadFile", 'r+')
        
    except IOError as e:
        print(e)
    else:
        print("Hurray we have successfully open the file let's write something")
        file1.write("Hello sir I am happy now to learn python its a long journey but")
        print(file1.tell())
        data=file1.read()
        print(data)
    return
MethodsOfFileOpening()
    
