# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=x/y 
    if k%2==0:
        print("YES")
    else:
        print("NO")