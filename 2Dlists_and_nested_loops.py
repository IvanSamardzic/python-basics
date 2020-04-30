#basic list 
#every item in list can be also a list, array
#thir grid has 4 rows and 3 columns, this is 2D list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#how to print just one values
print(number_grid[0][0]) #to print 1 from grid
print(number_grid[2][1]) #to print 8 from grid

#nested for loop
#how to print all the elements
for row in number_grid:
    for column in number_grid:
        print number_grid[row][column]  #to print all the elements in grid

