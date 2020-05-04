translator = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

in_digit = input("Phone: ")
output = ""
for ch in in_digit:
    output += translator.get(ch, "!") + " "
print(output)