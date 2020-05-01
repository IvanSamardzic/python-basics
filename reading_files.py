open("file_from_the_same_directory.txt","r") #just reading
open("file_from_the_same_directory.txt","w") #changing file
open("file_from_the_same_directory.txt","a") #append, cant change but can add
open("file_from_the_same_directory.txt","r+")#read and write

#to open a file
employee_file = open("file.txt","r")

#get infromation from the file
#check if the file is readable
print(employee_file.readable())

#to read infromation from file
print(employee_file.read())

#to read individual line
print(employee_file.readline())
print(employee_file.readlines()) #each line is now in the list

#use readlines with for loops
for employee in employee_file.readlines():
    print(employee)
    
#to close a file
employee_file.close()
