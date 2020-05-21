class A:
    @staticmethod
    def MethodA1():
        print('im A1')

    @staticmethod
    def MethodA2():
        print('Im A2')


class B(A):
    @staticmethod
    def MethodB1():
        print('Im b1')

    @staticmethod
    def MethodB2():
        print('im b2')


'''single level inhertnc'''
a1 = A()

a1.MethodA1()
a1.MethodA2()

b1 = B()
b1.MethodA1()
b1.MethodA2()
b1.MethodB1()
b1.MethodB2()


class C(B):
    @staticmethod
    def MethodC1():
        print('im C!')


''' Multi level inheritance '''
c1 = C()
c1.MethodB2()
c1.MethodB1()
c1.MethodA1()
c1.MethodA2()
c1.MethodC1()

'''------------------------'''


class D:
    @staticmethod
    def methodD():
        print('Im D')


class E:
    @staticmethod
    def methodE():
        print('Im E')


class F(D, E):
    @staticmethod
    def methodF():
        print('Im F')

    def __str__(self):
        self.methodF()


''' Multiple Inheritance'''

f = F()

f.methodD()
f.methodE()
f.methodF()


# polymorpism
# operator overloading

class G:
    @staticmethod
    def methodG():
        print('Im G')

    def methodGi(self):
        print('im gi')

    def __str__(self):
        self.methodGi()
        self.methodG()


g = G()
print(g)


