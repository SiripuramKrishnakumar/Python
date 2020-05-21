from abc import ABC, abstractclassmethod


class vivo(ABC):
    @abstractclassmethod
    def details(cls):
        pass


class vivo1(vivo):
    def details(cls):
        print('vivio1754')


v1 = vivo1()
v1.details()
