# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    k=a/x 
    p=b/y
    if k>p:
        print("Chefina")
    elif k==p:
        print("Both")
    else:
        print("Chef")