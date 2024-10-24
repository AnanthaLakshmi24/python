# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=list(map(int,input().split()))
    l=[]
    if (y*z)%x==0:
        l.append((y*z,x))
      
    if (x*z)%y==0:
       l.append((x*z,y))
      
    if (x*y)%z==0:
        l.append((x*y,z))
    
    if l:
        x,y=min(l)
        print(x,y)
     
    else:
        print(-1)