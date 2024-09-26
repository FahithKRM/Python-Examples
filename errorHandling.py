# use try, except in python
# in other languages as java, javascript try, catch

# try - code might execute the error
# exept - handle the error 
# finally - the error occure or not this is execute

# Ex : 01 - number divided by 0
"""
try :
    print("Try 1")
    result = 5/0
    print("Try 2")
    print(result)
    print("Try 3")
except Exception as e :
    print("Except 1")
    print(f"Error : {e}")
    print("Except 2")
finally : 
    print("Finally 1")
    print("Always execute this statement")
    print("Finally 2")
"""

# Ex 02 : Enter the input it is not digit occurr the error
try :
    print("Try 1")
    result = int(input())
    print("Try 2")
    print(result)
    print("Try 3")
except Exception as e :
    print("Except 1")
    print(f"Error : {e}")
    print("Except 2")
finally : 
    print("Finally 1")
    print("Always execute this statement")
    print("Finally 2")
