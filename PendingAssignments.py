# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x*y
    l=z*24*60
    if k<=l:
        print("YES")
    else:
        print("NO")