class Wanli:
    __name = 'wamli'
    __age = '18'

    def test_parent(self):
        print('hahaha')

    @property
    def age(self):
        print(self.__age)

    @age.setter
    def age(self, age):
        self.__age = age


class Wanli1(Wanli):
    pass


people = Wanli()
people.age
people.age = '20'
people.age
people1 = Wanli1()
people1.test_parent()
print(Wanli.__class__)


class A:
    pass


class A1(A):
    pass


class A2(A):
    pass


class B(A1, A2):
    pass


class C(A1, A2):
    pass


class D(B, C):
    pass


print(D.__mro__)
import sys
print(sys.path)
import time
tt = time.time()
print(tt)
print(time.ctime(tt))
print(time.localtime(tt))
import random
rr = random.randrange(1,10,2)
print(rr)
