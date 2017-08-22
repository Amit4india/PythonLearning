'''
Created on Aug 18, 2017

@author: amiti
'''
def FileRead():
    # this function define the method of how to open file and protect it using try Block
    try:
        file = open("C:\Eclipse\Workspace\LearningPython\SampleReadFile", 'r+')
        if file.name=="C:\Eclipse\Workspace\LearningPython\SampleReadFile":
            print(file.name)
        else:
            raise Exception
    except IOError: # Handling a specify error type
        print ("Unable to locate the file")
    except Exception:
        print ("file name is not matched")
    else: # this piece of code will only execute if try does through an error!
        file.write("hello amit how are you \n. We will become python master someday")
        print(file.readlines())
    finally: # This piece of code always run that's why we have put it close file in this block
        file.close
    return
FileRead()