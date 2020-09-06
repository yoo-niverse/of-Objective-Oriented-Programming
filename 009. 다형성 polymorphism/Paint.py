''' 다형성의 정의 파악 '''

from math import pi

class Rectangle:
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2*self.width + 2*self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle:
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)

class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Circle) or isinstance(shape, Rectangle):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])


paint_program = Paint()
rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

print(paint_program.total_perimeter_of_shapes())
print(paint_program.total_area_of_shapes())
''' 넓이 및 둘레를 구하는 상황에서 paint_program 변수에 들어가 있는 인스턴스가
원인지, 사각형인지 알 수없지만 정상적으로 동작함.

Rectangle과 Circle 클래스에 각각 area, perimeter 메소드가 모두 존재하기에 가능
즉, paint_program 변수는 원과 사각형 모두를 저장할 수 있는 다형성을 가지고 있음. '''
