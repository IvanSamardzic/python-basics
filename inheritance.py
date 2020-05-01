class Chef:
    def make_chicken(self):
        print("The chef  makes a chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes bby ribs")
        
#external file
class ChineseChef:
    def make_chicken(self):
        print("The chef  makes a chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes bby ribs")
    #functions that can only chinese chef
    def make_fried_rice(self):
        print("The chef makes fried rice")

form inheritance import Chef     
class ChineseChef(Chef): #inheritance is implemented using word "Chef" in brackets
    #functions that can only chinese chef
    def make_fried_rice(self):
        print("The chef makes fried rice")
        
        
#external file
from inheritance import Chef
myChef = Chef() #object creation
myChef.make_special_dish() #prints out string "The chef makes bby ribs"
myChineseChef = ChineseChef()
myChineseChef.make_chicken() #prints out string "The chef  makes a chicken"