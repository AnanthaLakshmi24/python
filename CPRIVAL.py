# cook your dish here
r1,r2=map(int,input().split())
d1,d2=map(int,input().split())
k=r1+d1 
p=r2+d2 
if k>p:
    print("Dominater")
else:
    print("Everule")