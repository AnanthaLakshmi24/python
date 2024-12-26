# cook your dish here
t=int(input())
for i in range(t):
    m,b=map(int,input().split())
    k=m//(b**2)
    if k<=18:
        print("1")
    elif k>18 and k<=24:
        print("2")
    elif k>24 and k<=29:
        print("3")
    else:
        print("4")