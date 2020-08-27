''' 정적 메소드를 활용하여 간단한 사칙연산 계산기 만들어보기 '''

class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        return (first_number + second_number)

    @staticmethod
    def subtract(first_number, second_number):
        return (first_number - second_number)

    @staticmethod
    def multiply(first_number, second_number):
        return (first_number * second_number)

    @staticmethod
    def divide(first_number, second_number):
        return (first_number / second_number)

    ''' static method는 인스턴스(또는 클래스) 변수를 사용하지 않고,
    단순 동작 수행 후 결과만 반환한다. 그 점을 이용하여 각 연산 메소드가
    파라미터로 받은 수치로 연산한 결과만 return 하도록 작성했다.'''


# 계산기 인스턴스 생성
calculator = SimpleCalculator()

# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
