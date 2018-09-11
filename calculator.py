"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def convertable(tokens):
    if len(tokens) == 3:
        try:
            int(tokens[1])
            int(tokens[2])
            return True
        except ValueError:
            print("Oops! That was not a valid number.")
            return False
    elif len(tokens) == 2:
        try:
            int(tokens[1])
            return True
           
        except ValueError:
            print("Oops! That was not a valid number.")
            return False
    else:
        print("Not enough arguments.")
        return False    


# Your code goes here
while True: 
    stir = input("> ")
    tokens = stir.split(" ")
    
    if tokens[0] == "q":
        break
    else:
        legit = convertable(tokens)
        if len(tokens) == 3 and legit:
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            if tokens[0] == "+" :
                print(add(num1,num2))
            elif tokens[0] == "-":
                print(subtract(num1,num2))      
            elif tokens[0] == "*":
                print(multiply(num1,num2))
            elif tokens[0] == "/":
                print(divide(num1,num2))
            elif tokens[0] == "power":
                print(power(num1,num2))
            elif tokens[0] == "mod":
                print(mod(num1,num2))
            else: 
                print ("Don't understand. Try again please.")

        elif len(tokens) == 2 and legit:
            num1 = int(tokens[1])
            if tokens[0] == "square":
                print(square(num1))
            elif tokens[0] == "cube":
                print(cube(num1))
            else: 
                print ("Don't understand. Try again please.")

        else: 
            print ("Don't understand. Try again please.")

