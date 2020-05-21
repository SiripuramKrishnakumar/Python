Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2//1.5
1.0
>>> 5//2
2
>>> 8*9/5
14.4
>>> 2**3
8
>>> print('kittu\'s laptop')
kittu's laptop
>>> 5*' kittu'
' kittu kittu kittu kittu kittu'
>>> 10*'kittu '
'kittu kittu kittu kittu kittu kittu kittu kittu kittu kittu '
>>> print('kittu\nsdf')
kittu
sdf
>>> print('r'kittu\nsdf')
      
SyntaxError: invalid syntax
>>> print(r'kittu\nsdf')
kittu\nsdf
>>> 
>>> 
>>> 
>>> ----------
SyntaxError: invalid syntax
>>> 
>>> name = 'krishna'
>>> name[5]
'n'
>>> name[-1]
'a'
>>> name[0:4]
'kris'
>>> len(name)
7
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list
<class 'list'>
>>> 
>>> 
>>> list1 = ['krish','M',22,638484786]
>>> list1
['krish', 'M', 22, 638484786]
>>> list1.append('Hyderabad')
>>> list1
['krish', 'M', 22, 638484786, 'Hyderabad']
>>> 
>>> list1.remove(22)
>>> list1
['krish', 'M', 638484786, 'Hyderabad']
>>> list1.pop(1)
'M'
>>> list1
['krish', 638484786, 'Hyderabad']
>>> list1.insert(1,'M')
>>> list1
['krish', 'M', 638484786, 'Hyderabad']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> del list1[1:2]
>>> list1
['krish', 638484786, 'Hyderabad']
>>> list1.extend[21,'sgfusgf']
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    list1.extend[21,'sgfusgf']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list1.extend([144,'fdg',54])
>>> list1
['krish', 638484786, 'Hyderabad', 144, 'fdg', 54]
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> nums = [54,6,56,63,4564,56,84,658,541,4]
>>> nums.sort()
>>> nums
[4, 6, 54, 56, 56, 63, 84, 541, 658, 4564]
>>> 
>>> 
>>> tuple
<class 'tuple'>
>>> tup1 = ('dfgd',5,46,65)
>>> tup1
('dfgd', 5, 46, 65)
>>> tup1[1]
5
>>> tup1[1] = 5
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tup1[1] = 5
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> set
<class 'set'>
>>> 
>>> 
>>> set1 = {12,56,45,4,54,77}
>>> set1
{4, 12, 45, 77, 54, 56}
>>> set2 = {4,5,5,5,45,78,87,54,45}
>>> set2
{4, 5, 45, 78, 54, 87}
>>> 
>>> set1[2]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
>>> 
>>> set1.add(454)
>>> set1
{4, 454, 12, 45, 77, 54, 56}
>>> set1
{4, 454, 12, 45, 77, 54, 56}
>>> 
>>> 
>>> dictionary
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    dictionary
NameError: name 'dictionary' is not defined
>>> Dictionary
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    Dictionary
NameError: name 'Dictionary' is not defined
>>> 
>>> 
>>> 
>>> data = {1:'krishna',2:'M',3:22,4:68764667}
>>> data[1]
'krishna'
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    data[0]
KeyError: 0
>>> data[4]
68764667
>>> data.get
<built-in method get of dict object at 0x000001F82BAEF640>
>>> data.get(1)
'krishna'
>>> data.get(0)
>>> print(data.get(0))
None
>>> print(data.get(1))
krishna
>>> any
<built-in function any>
>>> 
>>> keys = ['Name','Age','Gender','Ph no']
>>> values = ['ravan',25,'M',787336847]
>>> data1 = dict (zip(keys,values))
>>> data1
{'Name': 'ravan', 'Age': 25, 'Gender': 'M', 'Ph no': 787336847}
>>> data1[Name]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    data1[Name]
NameError: name 'Name' is not defined
>>> data1['Name']
'ravan'
>>> data1['Name']='krishna'
>>> data1
{'Name': 'krishna', 'Age': 25, 'Gender': 'M', 'Ph no': 787336847}
>>> del data1['Ph no']
>>> data1
{'Name': 'krishna', 'Age': 25, 'Gender': 'M'}
>>> 
>>> 
>>> 
>>> 
>>> setdata = {1:['dfsf',452] ,2: {21:fdsfsd,22:dsfsf,23:dsff}}
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    setdata = {1:['dfsf',452] ,2: {21:fdsfsd,22:dsfsf,23:dsff}}
NameError: name 'fdsfsd' is not defined
>>> setdata = {1:['dfsf',452] ,2: {21:'fdsfsd',22:'dsfsf',23:'dsff',4:[54,54,4,45,45]}}
>>> setdataa
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    setdataa
NameError: name 'setdataa' is not defined
>>> setdata
{1: ['dfsf', 452], 2: {21: 'fdsfsd', 22: 'dsfsf', 23: 'dsff', 4: [54, 54, 4, 45, 45]}}
>>> setdata[1]
['dfsf', 452]
>>> setdata[2][21]
'fdsfsd'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> list

help> LISTS

help> lists
No Python documentation found for 'lists'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> LISTS

help> LISTS

help> LISTS

help> BINARY

help> SCOPING

help> TYPES

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> LISTS

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help('LiSTS')
No Python documentation found for 'LiSTS'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('LISTS')

>>> help('LISTS')

>>> 
>>> 
>>> 
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> module
No Python documentation found for 'module'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> keyword
Help on module keyword:

NAME
    keyword - Keywords (from "Grammar/Grammar")

MODULE REFERENCE
    https://docs.python.org/3.8/library/keyword
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This file is automatically generated; please don't muck it up!
    
    To update the symbols in this file, 'cd' to the top directory of
    the python source tree and run:
    
        python3 -m Parser.pgen.keywordgen Grammar/Grammar                                       Grammar/Tokens                                       Lib/keyword.py
    
    Alternatively, you can run 'make regen-keyword'.

FUNCTIONS
    iskeyword = __contains__(...) method of builtins.frozenset instance
        x.__contains__(y) <==> y in x.

DATA
    __all__ = ['iskeyword', 'kwlist']
    kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'aw...

FILE
    c:\users\krish\appdata\local\programs\python\python38\lib\keyword.py


help> 