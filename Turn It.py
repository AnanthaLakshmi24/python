# cook your dish here
t=int(input())
for i in range(t):
    u,v,a,s=map(int,input().split())
    if u**2 - 2*a*s <= v**2:
        print("Yes")
    else:
        print("No")