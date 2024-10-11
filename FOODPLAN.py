# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x/10
    p=x-z
    if p>y:
        print("DINING")
    elif p<y:
        print("ONLINE")
    else:
        print("EITHER")