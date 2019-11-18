class Rectangle:
    length=0
    width=0
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
r1=Rectangle(3,4)
print(r1.area())
