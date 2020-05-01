#to get all the inf from the file
employee_file = open("file.txt", "r")
print(employee_file.read())
employee_file.close()

#to add new lines
#fot the first time it will be great, but for executing a file many times, every time it will be added
#string Toby - Humna Resources
employee_file = open("file.txt", "a")
employee_file.write("Toby - Human Resources")
employee_file.close()

#add string in the new line every time
employee_file = open("file.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

#to overwrite a file
employee_file = open("file.txt", "a")
employee_file.write("\nToby - Human Resources") #in the file there is only one string
