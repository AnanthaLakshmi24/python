from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def fun():
        pass
    @abstractmethod
    def fun2():
        pass
class B(A):
    def fun(self):
        pass
    def fun2(self):
        pass
    def dummy(self):
        print("HI")
obj=B()
obj.dummy()
        
