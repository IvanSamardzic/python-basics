#wait what the user will write
message = input(">")
#split input from the prompt whereever is white sign
words = message.split(" ")
emojis = {
    ":)" : "😄",
    ":(" : "😥",
    ";)" : "😉",
    ":D" : "😀"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#function definition
def greet_user():
    print("Hi there!")
    print("Welcome abroad!")
    
#function callin
print("Start")
greet_user()
print("Finish")