from xyz.supercoders.geometry.square import Square
from xyz.supercoders.geometry.rectangle import Rectangle
from xyz.supercoders.geometry.shape_stats import ShapeStatistics,Shape

side1 = Square(12)
side2 = Rectangle(34,56)
#print side1.area()
#print side1.perimeter()

print ShapeStatistics.get_stats(side1)

print 'Rectangle'

#print side2.area_of_rectangle()
#print side2.peri()

print ShapeStatistics.get_stats(side2)
#s = Shape()       This cannot be done now
