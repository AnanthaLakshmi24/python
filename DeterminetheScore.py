# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z= x//10
    print(z*y)