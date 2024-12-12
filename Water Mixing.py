# cook your dish here
t=int(input())
for i in range(t):
    p,d,h,c=map(int,input().split())
    s=0
    if p>=d:
        s=d+c 
        if s>=p:
            print("YES")
        else:
            print("NO")
    else:
        s=p+h
        if s>=d:
            print("YES")
        else:
            print("NO")