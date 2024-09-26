#defining function
"""def greeting():
    print("Welcome to the function")

greeting()
greeting()
greeting()"""

# positional functions
"""
def add(num1, num2):
    return num1 + num2

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

num1, num2 = map(int, input("Enter : ").split())

print("Add : ", add(num1, num2))
print("Sub : ", sub(num1, num2))
print("Mul : ", mul(num1, num2))
print("Div : ", div(num1, num2))
"""

# keyword functions -> can inter change the argument position
"""
def print_details(name, age):
    print(f"Name: {name}   Age: {age}")

print_details(age = 24, name = "Faahith")
"""

# lambda function 
 # var = lambda parameter : expression 
 # parameter : any number , expression : only one 

# Ex : 1
a = lambda : 5
print(a()) #has no parameter

# Ex : 2
b = lambda x : x ** 2
print(b(4)) 

# Ex : 3
c = lambda x : x
   