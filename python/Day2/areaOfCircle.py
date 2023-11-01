#Calculate the area and circumference of a circle given its radius
import math
def area(r):
     return math.pi*r*r
def circumference(r):
     return 2*math.pi*r
radius=int(input("enter the radius value:"))
print(area(radius))
print(circumference(radius))