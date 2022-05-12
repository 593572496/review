from multiprocessing import Process
from time import sleep


def test1():
    while True:
        sleep(1)
        print('test1')


def test2():
    while True:
        sleep(0.5)
        print('test2')


p1 = Process(target=test1)
