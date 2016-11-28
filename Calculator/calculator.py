from CalcCode import *

def showmenu():
    print "*****************************************"
    print "********* SUPER CALCULATOR 5000 *********"
    print "*****************************************"
    print ""
    print "Choose the operation you wish to perform: "
    print ""
    print "1. Addition"
    print "2. Subtraction"
    print "3. Multiplication"
    print "4. Division"
    print "5. Square Root"
    print "6. X to Power of Y"
    print "7. Factorial"
    print "8. Hypotenuse"
    print "9. Base-10 Logarithm"
    print "10. Modulo"
    print "11. Cube"
    print "12. Cube root"
    
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Get choice of operation
    
while True:
    print ""
    showmenu()   
    print ""
    str_input = raw_input("Please enter your choice, or 'q' to quit: ")
    if str_input == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif str_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']: # A list of all valid choices
        print ""
        print "Not a valid input. Please enter the number of your choice, or 'q' to quit: "
        print ""
        continue
    else:
        choice = str_input
    if choice in ['1', '2', '3', '4', '6', '8', '10']: # The operations that require TWO numbers
        while True:
            print ""
            str_input = raw_input("Please enter the first number: ")
            print ""
            try:
                numA = float(str_input)
                break
            except:
                print "Not a valid number."
                print ""
                continue
        while True:
            print ""
            str_input = raw_input("Please enter the second number: ")
            print ""
            try:
                numB = float(str_input)
                break
            except:
                print "Not a valid number."
                print ""
                continue
    else:                                             # Else, the operations requiring only ONE number.
        while True:
            print ""
            str_input = raw_input("Please enter the number: ")
            print ""
            try:
                numA = float(str_input)
                break
            except:
                print "Not a valid number."
                print ""
                continue
                
    # Call a function based on the choice of operation and print output to screen.
    
    if choice == '1':
        result = addition(numA, numB)
        print ""
        print "Adding {} plus {} equals {}." .format(numA, numB, result)
    elif choice == '2':
        result = subtract(numA, numB)
        print ""
        print "Subtracting {} from {} equals {}." .format(numA, numB, result)
    elif choice == '3':
        result = multiplication(numA, numB)
        print ""
        print "Multiplying {} by {} equals {}." .format(numA, numB, result)
    elif choice == '4':
        if numB == 0:
            print "Nice try - can't divide by zero!"
            continue
        result = division(numA, numB)
        print ""
        print "Dividing {} by {} equals {}." .format(numA, numB, result)
    elif choice == '6':
        result = power(numA, numB)
        print ""
        print "{} to the power of {} equals {}." .format(numA, numB, result)
    elif choice == '9' and numA > 0: # We only do positive logs around here.
        print ""
        result = log(numA)
        print "The logarithm to the base 10 of {} equals {}." .format(numA, round(result, 4))
    elif choice == '10':
        print ""
        result = mod(numA, numB)
        print "Non-integer values will be rounded."
        print "{} modulo {} equals {}." .format(round(numA,0), round(numB,0), result)
    elif choice == '5':
        print ""
        result = sqroot(numA)
        print "The square root of {} is {}." .format(numA, result)
    elif choice == '7':
        print "Rounding {} to integer." .format(numA)   # Rounding to integer because getting the factorial of 6.5 gave my program a hearty.
        numA = int(round(numA,0))
        result = factorial(numA)
        print "The factorial of {} equals {}." .format(numA, result)
    elif choice == '8':
        print ""
        result = hypotenuse(numA, numB)
        print "The hypotenuse length of a triangle of sides {} and {} equals {}." .format(numA, numB, round(result, 4))
    elif choice == '11':
        print ""
        result = cube(numA)
        print "The cube of {} equals {}." .format(numA, round(result, 4))
    elif choice == '12':
        print ""
        result = cubeRoot(numA)
        print "The cuberoot of {} equals {}." .format(numA, round(result, 4))
    else:                             # Catch cases where the number entered fails fo meet the criteria of the chosen operation.
        print ""
        print "Please make a valid entry for the chosen calculation."
        
 