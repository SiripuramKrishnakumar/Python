from threading import *
from time import sleep


class A(Thread):
    def run(self):
        for i in range(0, 10):
            print('A', i)
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(0, 10):
            print('B', i)
            sleep(1)


a = A()  # a thread
b = B()  # b thread

a.start()
sleep(0.3)
b.start()

a.join()
b.join()   # joining a , b threads to wait main threading

print('End')  # it will execute by main thread

