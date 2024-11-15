class Vector:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    def __add__(self, other):
        return self.a + self.b , other.a + other.b 
    def __sub__(self, other):
        return self.a - self.b , other.a - other.b
        
obj1 = Vector(5,8)
obj2 = Vector(9,10)
print(obj1 + obj2)
print(obj1 - obj2)
        