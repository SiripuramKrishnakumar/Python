Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> 
>>> x = sqrt(25)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x = sqrt(25)
NameError: name 'sqrt' is not defined
>>> x = math.sqrt(25)
>>> x
5.0
>>> print(math.floor)
<built-in function floor>
>>> print(math.floor(4.9))
4
>>> print(math.ciel(4.9))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(math.ciel(4.9))
AttributeError: module 'math' has no attribute 'ciel'
>>> print(math.ceil(4.9))
5
>>> print(math.ceil(4.1))
5
>>> print()

>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> print(math.pow(11,6))
1771561.0
>>> 
>>> import math as m
>>> print(m.pow(11,6))
1771561.0
>>> print(m.pow(11,6))
1771561.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from math import sqrt , pow
>>> pow(4,5)
1024.0
>>> sqrt(25)
5.0
>>> 
>>> 
>>> help('math')

>>> 