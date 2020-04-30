#getting two numbers to add

num1 = input("Enter a num: ")
num2 = input("Enter a num two: ")

result = num1 + num2

print(result)

#in previous example, python compiler will convert input numbers into strings

num1 = input("Enter a num: ")
num2 = input("Enter a num two: ")

result = int(num1) + int(num2)
print(result)

#there will be an error if you input non integer values

num1 = input("Enter a num: ")
num2 = input("Enter a num two: ")

result = float(num1) + float(num2)
print(result)

#now there wont be any problems 