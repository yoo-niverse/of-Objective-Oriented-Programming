''' 추상 클래스를 활용하여 정삼각형의 넓이와 둘레를 구하는 메소드 구현 '''

from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod # 추상 메소드를 의미하는 데코레이터
    def area(self) -> float: # Type Hinting 기능을 이용하여 메소드의 return 형식을 표기
        """도형의 넓이를 리턴한다: 추상 메소드이므로 자식 클래스가 반드시 Overriding 해야함. """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 추상 메소드이므로 자식 클래스가 반드시 Overriding 해야함. """
        pass


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape): # 추가하고자 하는 shape 인스턴스가 Shape 클래스의 인스턴스인지 검증
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])
            # 해당 도형 클래스에 정의된 area 메소드를 활용하여 넓이 계산

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])
            # 해당 도형 클래스에 정의된 perimeter 메소드를 활용하여 둘레 계산


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        ''' 부모 클래스인 Shape에서 정의된 추상 메소드 area를 overriding '''
        return self.base * self.height / 2

    def perimeter(self):
        ''' 부모 클래스인 Shape에서 정의된 추상 메소드 perimeter를 overriding '''
        return sqrt((self.base**2) + (self.height**2)) + self.base + self.height


# 테스트 코드
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

