num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    

operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
    int = (num1 + num2)
if operation == '-':
    int = (num1 - num2)
if operation == '*':
    int = (num1 * num2)
if operation == '/':
    int = (num1 / num2)
print("The result is: " + str(int))
