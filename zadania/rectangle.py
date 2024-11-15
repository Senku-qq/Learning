a = int(input("введите ширину прямоугольника: "))
b = int(input("введите длину прямоугольника: "))
class Rectangle:
    
    def __init__(self,width,length):
        self.width = width  
        self.length = length
    def area(self):
        area = self.width * self.length
        print(f"Площадь равна:{area}")
        return area
    def perimeter(self):
        perimeter = (self.width * 2) + (self.length * 2)
        print(f"Периметр равен:{perimeter}")
        return perimeter
priamougolnik = Rectangle(a,b)
priamougolnik.area()
priamougolnik.perimeter()
priamougolnik1 = Rectangle(a,b)
priamougolnik1.area()
priamougolnik1.perimeter()
