# cook your dish here
comp=int(input())
for c in range(comp):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=sum(a)-max(a)
    e=sum(b)-max(b)
    if(d>e):print("Bob")
    elif(d==e):print("Draw")
    else:print("Alice")
     