# cook your dish here
r,b = map(int,input().split())
g = 0
if (r == b):
    g = r
    print(5*g)
elif (r>b):
    g = b
    print((5*g)+(1*(r-b)))
else:
    g = r
    print((5*g)+(2*(b-r)))
