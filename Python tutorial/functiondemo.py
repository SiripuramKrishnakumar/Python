"""
def sample():
    print('hello')
    print('world')


sample()

def add(x,y):
    y= x+y
    print(y)

add(5,6)
add('jsdfh','dfsf')
add(45,56.14)

def prod(a,b):
    c = a*b
    return c

result = prod(5, 6)

print(result)


def add_sub(a,b):
    c = a+b
    d = a-b
    return c, d

result1 , result2 = add_sub(6,5)
print(result1,result2)
"""
from typing import List, Any, Union

''' pass by value and pass reference function argumrnts'''
# in python we don't use pass by value and pass reference
'''def update(x):
    x = 8
    print("X", x)


a = 10
print(id(a))
update(a)
print("a", a)
print(id(a))
'''


def person(name, age, gender, contact, city="Hyderabad"):
    print('name:', name)
    print('age:', age)
    print('gender:', gender)
    print('contact:', contact)
    print('city:', city)


person(45, 'male', 'krishna', 5436436)
# to overcome above issue position comes in to picture of actual arguments

person(age=20, name='krishna', contact=5436464, gender='male')


# city is optional parameter / argument
def person1(name, **data):
    print('name ', name)
    for i, j in data.items():
        print(i, j);


# here **data is a tuple

person1(age=20, name='krishna', contact=5436464, gender='male')


def sumnums(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)


# here *b is a tuple

sumnums(4, 56, 65, 6, 65, 65, 54)

a = 10


def test():
    global a
    print('global variable', a, id(a))
    a = 15
    print('local variable', a, id(a))


test()


def GetEvenOddCount(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


numlst = [5, 48, 46, 87, 46, 98, 36, 2, 7, 9, 1, 63, 19]

evn, odd =  GetEvenOddCount(numlst)

print("Even Count : {} and Odd count : {}".format(evn, odd))

