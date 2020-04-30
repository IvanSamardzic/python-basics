#creating a for loop
for letter in "Giraffe Academy":
    print(letter)
    
#create an array
#print all the friends names
friends = ["Jim", "Karen", "Kevin"]
for friend_name in friends:
    print(friend_name)

num = [0,1,2,3,4,5,6,7,8,9]
for index in num:
    print(index)

#specify to print all numbers lower than 10
for index in range(10):
    print(index)

#printing all numbers in range
for index in range(3,10):
    print(index)

#loop through the array
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(index)

#returning friends names
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
     else:
        print("not a first iteration")

