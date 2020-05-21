Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> a=10
>>> id(a)
140725179045824
>>> b=a
>>> id(b)
140725179045824
>>> 
>>> type(a)
<class 'int'>
>>> type(PI)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(PI)
NameError: name 'PI' is not defined
>>> PI = 3.14
>>> type(PI)
<class 'float'>
>>> k= float(5)
>>> k
5.0
>>>  c= complex(a,k)




SyntaxError: unexpected indent
>>>  c= complex(5,1
	    )
 
SyntaxError: unexpected indent
>>> c=complex(1,4)
>>> c
(1+4j)
>>> c = 5>6
>>> c
False
>>> type(c)
<class 'bool'>
>>> 
>>> k
5.0
>>> 
>>> 
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(False)
0
>>> lst = {4,45,45,45}
>>> type(lst)
<class 'set'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str = '
SyntaxError: EOL while scanning string literal
>>> str = ''
>>> type(str)
<class 'str'>
>>> lst = ['dsf',[45,45],'d']
>>> type(lst)
<class 'list'>
>>> range(0,10)
range(0, 10)
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> a = set(5,6,4'dfsf')
SyntaxError: invalid syntax
>>> a = set(5,6,5,4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a = set(5,6,5,4)
TypeError: set expected at most 1 argument, got 4
>>> 
>>> 
>>> a = range(1,55)
>>> print(a)
range(1, 55)
>>> list(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
>>> [a]
[range(1, 55)]
>>> set(a)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54}
>>> 
>>> d={a:45,b:54,c:45}
>>> d.keys()
dict_keys([range(1, 55), 10, False])
>>> d.values()
dict_values([45, 54, 45])
>>> d.keys()
dict_keys([range(1, 55), 10, False])
>>> 
>>> 
>>> 
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
>>> d.get('a')
>>> d
{range(1, 55): 45, 10: 54, False: 45}

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> operators
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    operators
NameError: name 'operators' is not defined
>>> 
>>> x=5
>>> y=5
>>> x*y
25
>>> y/5
1.0
>>> y//1
5
>>> y//x
1
>>> y/a
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    y/a
TypeError: unsupported operand type(s) for /: 'int' and 'range'
>>> y/1
5.0
>>> y//1
5
>>> y//5
1
>>> a,b = 5,6
>>> a
5
>>> b
6
>>> a<b
True
>>> a>b
False
>>> 
>>> 
>>> 
>>> a==b
False
>>> a != b
True
>>> a is b
False
>>> a is not b
True
>>> a<=b
True
>>> a>=b
False
>>> a>=b or a<b
True
>>> a>=5 or a<=5
True
>>> a>=1 or a<=1
True
>>> a>=1 and a>=1
True
>>> a<=1 and a>=1
False
>>> a <=1 & a>=1
False
>>> a<=1 | a>=1
True
>>> bin(10)
'0b1010'
>>> 0b0101
5
>>> oct(10)
'0o12'
>>> hex(10)
'0xa'
>>> oxa
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    oxa
NameError: name 'oxa' is not defined
>>> Oxa
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    Oxa
NameError: name 'Oxa' is not defined
>>> 0xa
10
>>> )xf
SyntaxError: unmatched ')'
>>> 0xf
15
>>> 