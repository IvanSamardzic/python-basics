#emoji_converter function definition
def emoji_converter(message):
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
    return output

#function callin
message = input(">")
print(emoji_converter(message))