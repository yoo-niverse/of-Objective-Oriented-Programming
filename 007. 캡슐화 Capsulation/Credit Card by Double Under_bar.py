''' __(더블 언더바)를 활용하여 클래스 내부 직접 접근 막기 '''
class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        ''' 인스턴스 생성 시 자동으로 실행되는 Dunder init 메소드에서
        자체적으로 파라미터를 변수에 설정하지 않고, 각 변수별 setter 메소드를 호출하여
        조건에 맞는지 1차 확인 후 값을 설정하도록 하였다. '''
        self.set_name(name)
        self.set_password(password)
        self.set_payment_limit(payment_limit)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"

    def set_password(self, password):
        self.__password = password

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, payment_limit):
        if 0 < payment_limit < CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())
