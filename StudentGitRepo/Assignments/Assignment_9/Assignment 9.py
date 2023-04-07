# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 4/9/23, 11:59 PM (CDT)
# MSITM 6341:
# Assignment : 9
# Assignment Title: working_with_classes
# working_with_classes.py

class Quadrilateral:
    def __init__(self,name,base,height):
        self.name = name
        self.base = base
        self.height = height

    def calculated_area(self):
        pass

class Trapezoid(Quadrilateral):
    def calculated_area(self):
        return ((self.base+self.base) /2) * self.height


class Rectangle(Quadrilateral):
    def calculated_area(self):
        return self.base * self.height

# 2 Instances of Trapezoid 
Trapezoid_instance_1 = Trapezoid("Trapezoid_1:-",3,4)
print(Trapezoid_instance_1.name, Trapezoid_instance_1.calculated_area())

Trapezoid_instance_2 = Trapezoid("Trapezoid_2:-",4,5)
print(Trapezoid_instance_2.name, Trapezoid_instance_2.calculated_area())
# 3 Instances of Rectangle

Rectangle_instance_1 = Rectangle("Rectangle_1:-",6,2)
print(Rectangle_instance_1.name, Rectangle_instance_1.calculated_area())

Rectangle_instance_2 = Rectangle("Rectangle_2:-",4,5)
print(Rectangle_instance_2.name, Rectangle_instance_2.calculated_area())

Rectangle_instance_3 = Rectangle("Rectangle_3:-",6,3)
print(Rectangle_instance_3.name, Rectangle_instance_3.calculated_area())

