from numpy import *

"""arr = array([1, 5, 6, 56])
print(arr)
print(arr.dtype)

arr1 = array([1,5,2.5])
print(arr1)
print(arr1.dtype)
"""
'''numpy linspace '''
'''
arr3 = linspace(1,15,25)
print(arr3)
'''
'''arr3 = linspace(1,15)
print(arr3)
'''
"""arr4 = arange(1,12,2)
print(arr4)
"""'''it skip the 2 nums and print 1 to 15'''

arr5 = zeros(5)
'''print 5 zeros'''
# print(arr5)

arr6 = ones(5)
'''print 5 ones'''
# print(arr6)

arr7 = array([5, 10, 15])
arr7 = arr7 + 5
'''adding 5 to each element'''
"""print(arr7)

print(min(arr7))
print(max(arr7))
print(sqrt(arr7))
print(pow(arr7, 2))
print(log(arr7))
arr8 = array([25,20,35])
print(concatenate([arr7,arr8]))
"""
# arr9 = arr7.view() shellow copy

"""arr9 = arr7.copy()
''' deep copy'''
print(arr7)
print(arr9)
print(id(arr7))
print(id(arr9))
"""
# multidimensional array
arr8 = array([
    [1, 5, 6],
    [4, 7, 56]
    ])

print(arr8)
print(arr8.ndim)
print(arr8.shape)
print(arr8.size)

arr9 = arr8.flatten()
'''convert 2 dim to one dim array'''
# print(arr9)

m1 = matrix('1 2 5; 8 2 3; 7 4 5')
m2 = matrix('2 5 9; 4 3 7; 2 7 1')
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)
