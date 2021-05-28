import art
import os

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b
    
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)
    first_number = int(input("What is the first number?\n"))
    should_continue = True
    
    while should_continue:
        operator = input("Choose an operation +, -, *, /\n")
        next_number = int(input("What is the next number?\n"))
        result = operations[operator](first_number,next_number)
        print(f"{first_number} {operator} {next_number} = {result}")
        
        if input(f"If you would like to continue with {result} type 'y' or any other key to start over\n") == "y":
            first_number = result
        else:
            should_continue == False
            os.system("clear")
            calculator()
            
calculator()            