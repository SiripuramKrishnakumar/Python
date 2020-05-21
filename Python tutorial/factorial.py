def fact(n):
    if n > 0:
        a = 1
        for i in range(1, n):
            a *= n
            n = n - 1

        print(a)

    else:
        print('Enter a number greater than 0')


fact(5)



# by recursion

def factRec(n):
    if n == 0:
        return 1

    return n * factRec(n - 1)


print(factRec(5))
