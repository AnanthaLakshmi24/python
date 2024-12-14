# cook your dish here
t=int(input())
for i in range(t):
    x,a,y,b=map(int,input().split())
    k=x/a 
    p=y/b 
    if k==p:
        print("Equal")
    elif k>p:
        print("Alice")
    else:
        print("Bob")