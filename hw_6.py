# НОМЕР 1
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print(f"Площадь прямоугольника равна: {self.a * self.b}")

    def perimeter(self):
        print(f"Периметр прямоугольника равен: {(self.a + self.b) * 2}")

rect_1 = Rectangle(5, 10)
rect_1.area()
rect_1.perimeter()

# НОМЕР 2
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Площадь круга равна: {3.14 * self.radius ** 2}")

    def perimeter(self):
        print(f"Периметр круга равен: {2 * 3.14 * self.radius}")

circle_1 = Circle(5)
circle_1.area()
circle_1.perimeter()

# НОМЕР 3
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Площадь треугольника равна: {0.5 * self.base * self.height}")

triangle_1 = Triangle(3, 4)
triangle_1.area()

