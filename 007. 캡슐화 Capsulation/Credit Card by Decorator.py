''' 데코레이터를 이용하여 캡슐화 '''
class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
            '''언더바 1개를 사용하여 개발자 및 사용자에게 변수로의 직접 접근을 경고한다.
            하지만 강제로 접근을 막는 효과는 없다.'''
        self.name = name
        self._password = password # _password 변수에 password 메소드를 호출하여 password 값을 설정한다.
        self._payment_limit = payment_limit # password와 동일한 원리


    @property # password getter 메소드
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @password.setter # password setter 메소드
    def password(self, password):
        self._password = password

    @property # payment getter 메소드
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter # payment setter 메소드
    def payment_limit(self, payment_limit):
        if 0 < payment_limit < CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.name) # card 인스턴스의 name 변수를 출력하라
print(card.password) # card 인스턴스의 password 메소드를 호출하라
print(card.payment_limit) # card 인스턴스의 payment_limit 메소드를 호출하라

card.name = "성태호" # card 인스턴스의 name 변수를 설정하라
card.password = "1234" # card 인스턴스의 password 메소드를 호출하고, 1234를 파라미터로 넘겨서 설정하라.
card.payment_limit = -10 # card 인스턴스의 payment_limit 메소드를 호출하고, -10을 파라미터로 넘겨서 설정하라.

print(card.name)
print(card.password)
print(card.payment_limit)
