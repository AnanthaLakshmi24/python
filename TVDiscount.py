# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    k=abs(a-c)
    z=abs(b-d)
    if k<z:
        print("First")
    elif k>z:
        print("Second")
    else:
        print("Any")