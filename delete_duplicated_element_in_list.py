#create 2 lists, one with numbers nad one empty
numbers = [1, 2, 3, 4, 5, 5, 4, 4, 6, 7, 8, 8]
uniques = []
for number in numbers: #iterate over the list
    if number not in uniques: #if number is not already in the second list
        uniques.append(number) #insert new number in the second list
print(uniques) #at the end print new list