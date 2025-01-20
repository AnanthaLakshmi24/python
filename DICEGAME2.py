# cook your dish here
t=int(input())
for i in range(t):
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    ax=a1+a2 
    ay=a2+a3 
    az=a3+a1 
    bx=b1+b2 
    by=b2+b3
    bz=b3+b1
    k=max(ax,ay,az)
    p=max(bx,by,bz)
    if k>p:
        print("Alice")
    elif k<p:
        print("Bob")
    else:
        print("Tie")