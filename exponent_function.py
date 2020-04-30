#defining the function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range (0,pow_num -1):
        result *= base_num
        return result
        
#printing the result
print(raise_to_power(2,7)) #to get 128
print(raise_to_power(3,4)) #to get 81

#or you can do

res = raise_to_power(2,7)
print(res) #to get 128