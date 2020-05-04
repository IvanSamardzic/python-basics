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
    