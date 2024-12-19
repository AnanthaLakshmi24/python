# cook your dish here
r,o,c=map(int,input().split())
l=20-o
k=l*6 
m=k*6 
b=c+m 
if b>r:
    print("YES")
else:
    print("NO")