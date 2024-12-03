# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    z=0
    o=0
    for k in range(3):
        if l[k]==0:
            z=z+1
        else:
            o=o+1
    if z>=2:
        print("Water filling time")
    else:
        print("Not now")