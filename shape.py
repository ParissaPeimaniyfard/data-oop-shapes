'''test classes'''
class Shape:
    """ this is the shape class """
    def __init__(self, color, name):
        """ set initial values """
        self.shape_name = name
        self.shape_color = color

    def say_name(self):
        """ Print the value """
        print ("My name is", self.shape_name)

test= Shape ("blue","xyz")
test.say_name()

class Rectangle (Shape):
    ''' this is rectangle class'''
    def __init__(self, color, name, width, height):
        ''' set parameters'''
        Shape.__init__(self,color,name)
        #self.recName= name
        self.rec_width= width
        self.rec_height= height

    def say_name(self):
        ''' print the name'''
        Shape.say_name(self)
        print ("My name is", self.shape_name, "and I am a rectangle")

    def area_rec(self):
        ''' calculate rectangle area'''
        self.rec_area=self.rec_height*self.rec_width
        print ("Area:", self.rec_area)

    def perimeter(self):
        ''' calculate rectangle perimeter'''
        self.rec_perimeter= (self.rec_height+self.rec_width)*2
        print ("Perimeter:", self.rec_perimeter)

test2= Rectangle ("red","Rei", 8, 9)
test2.say_name()
test2.area_rec()
test2.perimeter()

class Circle (Shape):
    ''' circle class'''
    def __init__(self, color, name, radius):
        ''' set the parameters'''
        Shape.__init__(self,color,name)
        #self.circName= name
        self.radius_circle = radius

    def say_name(self):
        '''print the name'''
        Shape.say_name(self)
        print ("My name is", self.shape_name, "and I am a circle")

    def area_circle(self):
        '''calculate circle area'''
        self.cirarea= 3.14 * self.radius_circle * self.radius_circle
        print ("Area:", self.cirarea)

    def perimeter_circle(self):
        ''' calculate circle perimeter'''
        return 2 * 3.14 * self.radius_circle

test3= Circle("yellow","klot", 3)
test3.say_name()
test3.area_circle()
test3.perimeter_circle()
