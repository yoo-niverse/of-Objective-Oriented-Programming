''' init 메소드와 str 메소드 활용해보기 '''
class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price
            # init 메소드는 초기화의 역할을 수행하며, 인스턴스 생성 시 자동 호출되어 인스턴스 변수의 값을 초기화한다.

    def __str__(self):
        return (f'{self.name} 가격: {str(self.price)}')
            # str 메소드는 print문 사용 시 자동 호출되며, 출력문의 형태 지정 등에 사용된다.

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)
