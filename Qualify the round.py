# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=y+(z*2)
    if x<=k:
        print("Qualify")
    else:
        print("NotQualify")