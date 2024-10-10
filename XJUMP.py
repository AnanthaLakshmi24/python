# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    p=x//y 
    q=x%y
    print(p+q)