''' 추상 클래스를 활용하여 주행 시뮬레이터 프로그램 구현하기 '''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, speed):
        self._speed = speed

    @property
    @abstractmethod
    def speed(self, speed):
        pass

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self._speed = 0

print(Vehicle.mro())
print(dir(Vehicle))
