# cook your dish here
l=int(input())
b=int(input())
area = l*b
peri = 2*(l+b)
if area<peri:
    print("Peri")
    print(peri)
elif area>peri:
    print("Area")
    print(area)
else:
    print("Eq")
    print(area)