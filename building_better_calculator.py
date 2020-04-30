#setting the operands
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

#setting the operator
op = input("Enter operator: ")

#monitor the operator sign
if op == "+":
    printf(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")