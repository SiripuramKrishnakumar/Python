
print('Enter the numbers')
a = 5 # int(input())
b = 0 # int(input())

try:
    print('Connection open')
    print(a/b)
except ZeroDivisionError as z:
    print('number can not divide by 0')
except Exception as e:
    print('Error', e)
finally:
    print('Connection closed')
