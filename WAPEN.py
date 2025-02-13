# cook your dish here
x,y=map(int,input().split())
if 1<=x<=150 and 0<=y<=10:
    y=y*10
    c=x+y
    
print(c)
