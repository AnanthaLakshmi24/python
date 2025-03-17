# cook your dish here
for _ in range(int(input())):
    x,y,z,a,b,c=map(int,input().split())
    h=0
    for i in range(z):
        if c>0:
            c-=1
            h+=1
        elif b>0:
            b-=1
            h+=1
        elif a>0:
            a-=1
            h+=1
    for i in range(y):
        if b>0:
            b-=1
            h+=1
        elif a>0:
            a-=1
            h+=1
    for i in range(x):
        if a>0:
            a-=1
            h+=1
    print(h)