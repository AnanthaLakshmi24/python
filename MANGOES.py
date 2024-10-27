# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    p=z-y
    q=p//x 
    print(q)