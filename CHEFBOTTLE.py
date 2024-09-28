# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    p=z//y 
    if x>p:
       print(p)
     
    else:
        print(x)