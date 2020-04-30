#defining the function
def cube(num):
    return num * num * num
    
#calling the function
print(cube(3))
print(cube(4))

#variable defining
result = cube(4) # to get 64
print(result)

is_male = True
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")#logical error, nothing is printing


is_male = False
if is_male:
    print("You are a male")
else: 
    print("You are not a male")
    
is_male = True
is_tall = True 
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

is_male = True
is_tall = True 
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")
    
s_male = True
is_tall = True 
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male and tall")
else:
    print("You are not a male and not tall")