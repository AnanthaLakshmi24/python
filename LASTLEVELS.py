# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if x<=3:
        print(x*y)
    else:
        p=x//3
        n=p*3
        remain=x-n
        if remain!=0:
            remaintime=remain*y
            breakt=p*z
            level=n*y 
            total=breakt+level+remaintime 
            print(total)  
        else:
            breakt=p*z
            level=n*y 
            total=breakt+level 
            print(total-z) 