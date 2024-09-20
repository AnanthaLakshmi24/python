# cook your dish here
x,y,k=map(int,input().split())
s=abs(x-y)
if s<=k:
    print("Yes")
else:
    print("No")
    