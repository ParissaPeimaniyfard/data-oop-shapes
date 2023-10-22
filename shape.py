class shape:
    def __init__(self, color, name):
        self.shapeName = name
        self.shapeColor = color
    def say_name(self):
        print ("My name is", self.shapeName)

test= shape ("blue","xyz")
test.say_name()

class Rectangle (shape):
    def __init__(self, color, name, width, height):
        shape.__init__(self,color,name)
        #self.recName= name
        self.recWidth= width
        self.recHeigh= height

    def say_name(self):
        shape.say_name(self)
        print ("My name is", self.shapeName, "and I am a rectangle")

    def areaRec(self):
        self.recArea=self.recHeigh*self.recWidth
        print ("Area:", self.recArea)

    def perimeter(self):
        self.recPerimeter= (self.recHeigh+self.recWidth)*2
        print ("Perimeter:", self.recPerimeter)

test2= Rectangle ("red","Rei", 8, 9)
test2.say_name()
test2.areaRec()
test2.perimeter()

class Circle (shape):
    def __init__(self, color, name, radius):
        shape.__init__(self,color,name)
        #self.circName= name
        self.radiusCircle= radius

    def say_name(self):
        shape.say_name(self)
        print ("My name is", self.shapeName, "and I am a circle")

    def areaCircle(self):
        self.Cirarea= 3.14 * self.radiusCircle * self.radiusCircle
        print ("Area:", self.Cirarea)

    def perimeterCircle(self):
        self.perimeterCircle= 2 * 3.14 * self.radiusCircle
        print ("Perimeter:", self.perimeterCircle)

test3= Circle("yellow","klot", 6)
test3.say_name()
test3.areaCircle()
test3.perimeterCircle()
