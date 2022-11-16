from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_2.get_area_square())
print(square_1.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

circle_1 = Circle(6)
circle_2 = Circle(15)

print(circle_1.get_square_circle())

