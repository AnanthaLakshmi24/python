# cook your dish here
t=int(input())
for i in range(t):
    x,y,p=map(int,input().split())
    total=4*y-x
    if total>=p:
        print("PASS")
    else:
        print("FAIL")