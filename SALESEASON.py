# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x<=100:
        print(x)
    elif x>=100 and x<=1000:
        x=x-25
        print(x)
    elif x>=1000 and x<=5000:
        x=x-100
        print(x)
    else:
        x=x-500
        print(x)