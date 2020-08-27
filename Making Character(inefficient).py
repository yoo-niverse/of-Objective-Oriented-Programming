''' 클래스와 객체를 활용하여 게임 캐릭터 만들기(비효율적 코드) '''
class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
        self.name = str(name)
        self.hp = hp
        self.power = power

    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        return (self.hp > 0)

    def get_attacked(self, damage):
        """
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
        """
        if is_alive(self):
            if damage < self.hp:
                self.hp -= damage
            else:
                self.hp = 0
        else:
            print("{}은 이미 죽었습니다.".format(self.name))


    def attack(self, other_character): #''' get_attacked 메소드의 동일 기능을 반복 열거하고 있다. '''
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
       if other_character.hp > self.power:
           other_character.hp -= self.power
       else:
           other_character.hp = 0

    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.
        if self.hp == 0:
            print("{}은 이미 죽었습니다.".format(self.name))
        return (f'{self.name}님의 hp는 {self.hp}만큼 남았습니다.')

# 게임 캐릭터 인스턴스 생성
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)
