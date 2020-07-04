# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

value1 = int(input('Enter number 1: '))
value2 = int(input('Enter number 2: '))
operator = input('Enter operator (+, -, *, /): ')


def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return 'division by zero error'
        return a / b
    else:
        return 'Operator not recognized'


print(calculator(value1, value2, operator))
