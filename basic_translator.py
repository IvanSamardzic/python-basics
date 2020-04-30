#Giraffe Language
#vowels -> g
#------------
#all vowels become char g

#define a function
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

#print new language word
print(translate(input("Enter a phrase: ")))

#or

#define a function
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

#print new language word
print(translate(input("Enter a phrase: ")))


#or to leave uppercase and lowercasee chars

#define a function
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

#print new language word
print(translate(input("Enter a phrase: ")))