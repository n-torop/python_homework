import math

class Point:
    def __init__(self, x, y):
        self.y=y
        self.x=x
        
    def __eq__(self, other):
        if not isinstance(other, Point): 
            return NotImplemented
        return self.x==other.x and self.y==other.y
        

    def __str__(self):
        return f"(Point {self.x},{self.y})"
    
    def euclidean(self, other):
        return math.hypot(self.x-other.x, self.y-other.y)
       
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"(Vector: {self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)
        return NotImplemented

p1=Point(1, 2)
p2=Point(4, 3)
p3=Point (1,3)


print (p1)
print(p1==p2)
print(p1.euclidean(p2))

v1=Vector(3,4)
v2=Vector (5,6)

print (v1)
v3=v1+v2
print (v3)


