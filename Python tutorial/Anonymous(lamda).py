from typing import List, Any, Union

s = lambda a: a * a

print(s(5))

a = lambda x, y: x + y

print(a(6, 4))

# filter , reduce , map functions

numlst = [2, 4, 5, 5, 6, 8, 7, 6, 8, 15, 45, 68, 87, 687, 87, 68, 786]

even = list(filter(lambda a: a % 2 == 0, numlst))

print(even)

doubles = list(map(lambda a: a * 2, numlst))
print(doubles)

from functools import reduce

addListNums = reduce(lambda a, b: a + b, numlst)
print(addListNums)


