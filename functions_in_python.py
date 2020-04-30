#defining the function
def say_hi():
    print("Hello User!")

#calling the function
say_hi() 


#defining the function
def say_hi(name1):
    print("Hello " + name1 + "!")

#calling the function
say_hi("Mike") 

#defining the function
def say_hi(name1, name2):
    print("Hello " + name1 + "!")
    print("Hello " + name2 + "!")
    
#calling the function
say_hi("Mike", "Philip", "21", "19") 


#defining the function
def say_hi(name1, name2, age1, age2):
    print("Hello " + name1 + "!")
    print("You are " + age1)
    print("Hello " + name2 + "!")
    print("You are " + age2)

    
#calling the function
say_hi("Mike", "Philip", "21", "19") 

#defining the function
def say_hi(name1, name2, age1, age2):
    print("Hello " + name1 + "!")
    print("You are " + str(age1))
    print("Hello " + name2 + "!")
    print("You are " + str(age2))

    
#calling the function
say_hi("Mike", "Philip", 21, 19) 