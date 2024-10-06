# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x==y==z==0:
        print("Water filling time")
    elif x==y==z==1:
        print("Not now")
    elif x==y==0 or x==z==0 or y==z==0:
        print("Water filling time")
    else:
        print("Not now")