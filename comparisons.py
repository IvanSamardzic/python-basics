#defining the function
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
       print("num1 is the largest number")
    elif num2 >= num1 and num2 >= num3:
        print("num2 is the largest number")
    else:
        print("num3 is the largest number")

#calling the function  
print(max_num(3,4,5))

#we can also compare strings, booleans, integers etc.
