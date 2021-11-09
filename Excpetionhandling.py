##intcntr = 0

##raise keyword for exception handling
##if intcntr !=1:
  ##  pass
   # raise Exception("Item counter is not 1")

##assert(intcntr==1)

## try block will take the error and control will be moved to except block
try:
    with open('file1.txt','r') as reader:
        line1 = reader.read()
        print(lin1)

##except Exception as will allow uswer to move the excpetion value into variable
except Exception as p:
    print(p)

#No matter failure or no failure, finally block will be excuted
## best used when u want to close objects or cleaning up all the records
finally:
    print("Execution ends here")
