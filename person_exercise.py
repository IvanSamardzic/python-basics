class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi I'm " + self.name + ", how are you?")
        
person1 = Person("John Adams")
print(person1.talk()) #in prompt it will be written Hi I'm John Adams, how are you?

person2 = Person("Robert Berg")
print(person2.talk())