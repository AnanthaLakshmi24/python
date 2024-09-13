a=float(input("enter value of a"))
b=float(input("enter value of b"))
c=float(input("enter value of c"))
s=(a+b+c)/2
area  = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('area of triangle is %0.2f' %area)