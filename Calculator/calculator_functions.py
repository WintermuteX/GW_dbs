import math    # Importing the math module to demonstrate I know it exists and how to use it.

def subtract(num1, num2):
    return num1 - num2    

def addition(num1, num2):
    return num1 + num2
    
def multiplication(num1, num2):
    return num1 * num2
    
def division(num1, num2):
    return num1/num2

def sqroot(num1):
    return math.sqrt(num1)    # applying a function from the imported math module
    
def power(num1, num2):
    return num1 ** num2  
    
def factorial(num1):    # recursive algorithm example covered in class
    if num1 == 1:
        return 1
    else:
        return num1 * factorial(num1-1)

def hypotenuse(num1, num2):
    return sqroot(num1*num1 + num2*num2) # calling square root function from this code for the heck of it
    
def cube(num1):
    return num1 * num1 * num1 

def log(num1):
    return math.log10(num1)

def mod(num1, num2):
    round(num1,0)   # rounding the numbers to integers
    round(num2,0)
    return int(num1) % int(num2)
    
def cubeRoot(num1):
    if num1 >= 0:   # for positive cube roots
        return num1**(1./3)
    elif num1 < 0:  # getting the absolute value of negative cube roots and making it negative
        return -(abs(num1)**(1./3))

