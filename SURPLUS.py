# cook your dish here
t=int(input())
for i in range(t):
    a1,a2,b1,b2=map(int,input().split())
    e=a1+b1 
    i=b2+a2
    c=e-i 
    if c<0:
        print("YES")
    else:
        print("NO")