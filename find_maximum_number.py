#function definition
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max       

#list definition and function callin     
num = [2,5,9,12,1,13,92]
max_num = find_max(num)
print(max_num) #it prints out max number in a list