class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
        
point1 = Point(10,20) #x is 10, y is 20
point1.x = 11 #x is changed to 11
print(point1.x) #print x object variable
print(point1.draw()) #run object method