# Program for a simple calculator

# Addition function 
def add(x, y) :
    return x + y

# Subtraction function 
def subtract(x, y) :
    return x - y

# Multiplication function 
def multiply(x, y) :
    return x * y

# Division function
def divide(x, y) :
    return x / y

# Modulas Operation function 
def mod(x, y) :
    return x % y

print('Select an operation: ')
print('1. Add')
print('2. Subract')
print('3. Multiply')
print('4. Divide')
print('5. Mod')

# take input from the user
operation = input('Enter choice(1/ 2/ 3/ 4/ 5) : ')

# check if operation is one of five options
if operation in ('1', '2', '3', '4', '5') :
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

if operation == '1' :
    print(num1, '+', num2, '=', add(num1, num2))
elif operation == '2' :
    print(num1, '-', num2, '=', subtract(num1, num2))
elif operation == '3' :
    print(num1, '*', num2, '=', multiply(num1, num2))
elif operation == '4' :
    print(num1, '/', num2, '=', divide(num1, num2))
elif operation == '5' :
    print(num1, '%', num2, '=', mod(num1, num2))

else :
    print('Invalid input')

