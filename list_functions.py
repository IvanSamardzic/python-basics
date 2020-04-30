lucky_numbers = [4,8,15,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

#to combine two lists together
friends.extend(lucky_numbers)
print(friends)

#to add element
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")

#to add element in the middle of list
friends.insert(1, "Kelly") #Kelly as a second element
print(friends)

#to remove element
friends.remove("Jim")
print(friends)

#to clear list
friends.clear()
print(friends)

#to get rid of last element
friends.pop()
print(friends)

#to check any element, returning its index
print(friends.index("Oscar"))

#count the number of the same elements
friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
print(friends.count("Karen"))

#to sort the list
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

#to reverse the list
lucky_numbers.reverse()
print(lucky_numbers)

#to copy the list
friends_too = friends.copy()
print(friends_too)
