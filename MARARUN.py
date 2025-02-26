# cook your dish here
for i in range(int(input())):
    D,d,a,b,c=map(int,input().split())
    dist=d*D
    if dist>=10 and dist <21:
        print(a)    
    elif dist>=21 and dist<42:
        print(b)
    elif dist>=42:
        print(c)
    elif dist<10:
        print(0)    