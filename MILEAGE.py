# cook your dish here
t=int(input())
for i in range(t):
    n,x,y,a,b=map(int,input().split())
    k=(n/a)*x
    s=(n/b)*y 
    if k<s:
        print("PETROL")
    elif k==s:
        print("ANY")
    else:
        print("DIESEL")