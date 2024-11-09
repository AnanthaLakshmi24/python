class A:
    def a(self):
        print("I am at class-A")
class B(A):
    def b(self):
        print("I am at class-B")

class C(A):
    def c(self):
        print("I am at class-C")

class D(B,C):
    def d(self):
        print("I am at class-D")

class E(D):
    def e(self):
        print("I am at class-E")

obj1=B()
obj2=C()
obj3=D()
obj4=E()
obj4.d()
obj4.c()
obj4.b()
obj4.a()


        
